from class_object import *
import sqlite3
import re
import tkinter as tk
from tkinter import messagebox,StringVar
from datetime import datetime
import pandas as pd
import xlsxwriter


def executeSQL(query:str,datos:tuple=()):
    conn = sqlite3.connect('LoteDB.db')
    cursor = conn.cursor()
    cursor.execute(query, datos)
    registros = cursor.fetchall()
    conn.commit()
    conn.close()
    return registros


def registerSQL(nombre,deuda,telefono):
    cliente = Cliente(nombre,deuda,0,telefono)
    query = 'INSERT INTO clientes (nombre, deuda, telefono, ganancia) VALUES (?, ?, ?, ?)'
    datos = (str(cliente.nombre),float(cliente.deuda),str(cliente.telefono),float(cliente.ganancia))
    executeSQL(query,datos)

def id_clients():
    unaQuery = """
        SELECT id, nombre
        FROM clientes
        ORDER BY nombre ASC
    """
    registros = executeSQL(unaQuery)

    return registros

def obtenerValorParentesis(cadena):
    patron = r'\((.*?)\)'  # Expresión regular para buscar cualquier cosa entre paréntesis

    resultado = re.search(patron, cadena)
    if resultado and resultado.group(1).isnumeric():
        return int(resultado.group(1))
    messagebox.showerror("Error","Por favor asegurarse de que eligió un jugador de la lista")
    return

def isNumericEntry(value):
    if value.isdigit() or value == "":
        return True
    else:
        return False

def isNumericEntryFloat(value):
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

def obtenerCliente(id):
    query = f"""
    SELECT *
    FROM clientes
    WHERE id = '{id}'
    """
    cliente = executeSQL(query)
    if(len(cliente)>0):
        return cliente[0]

def bet(cliente,valor,turno,loteria,pagado,numero):
    jugada = Jugada(cliente,valor,loteria,pagado,turno,numero)
    query = f"""INSERT INTO jugadas (cliente, numero, precio, loteria, turno, fecha, vigencia, pago, cobrado) VALUES (?,?,?,?,?,?,?,?,?)"""
    datos = (cliente.nombre,jugada.numero,jugada.precio,jugada.loteria,jugada.turno,jugada.fecha,True,jugada.pagado,False)
    executeSQL(query,datos)
    return jugada

def playBets(id,num,valor,turnos,loterias,pagado):

    respuestaConsulta = obtenerCliente(id)
    if(respuestaConsulta==None):
        messagebox.showwarning("Atención","Asegurese de haber ingresado un ID existente")
        return
    cliente = Cliente(respuestaConsulta[1],respuestaConsulta[2],respuestaConsulta[3],respuestaConsulta[4],int(id))
    apuestas = []
    deudaActual = cliente.deuda

    for turno, suValor in turnos.items():
        if suValor:
            for loteria, suValor_ in loterias.items():
                if suValor_:
                    apuestas.append(bet(cliente,valor,turno,loteria,pagado,num))
                    if not pagado:
                        deudaActual+=valor
                        
    query = f"""UPDATE clientes SET deuda={deudaActual} WHERE id={cliente.id}"""
    executeSQL(query)
    return apuestas

def esElMismoApostador(apuestas,idApostador):
    ids = list(set(map(lambda apuesta: int(apuesta.apostador.id),apuestas)))
    try:
        return ids[0] == idApostador
    except IndexError:
        return True

def printTicket(text):
    print("Imprimiendo")

def windowTicket(textPrint):
    ventana = tk.Toplevel()
    ventana.resizable(False,False)
    comentario = tk.Text(ventana,width=35,height= 20)
    comentario.insert(tk.END, textPrint)

    retorno = StringVar(value="")
    def aux(textPrint):
        printTicket(textPrint)
        retorno.set("True")
        ventana.withdraw()
    def aux2():
        retorno.set("True")
        ventana.withdraw()

    scrollbar = tk.Scrollbar(ventana) #Se crea scrollbar y se asocia al comentario
    scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
    comentario.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=comentario.yview)

    comentario.config(state=tk.DISABLED)
    comentario.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)

    tk.Button(ventana,text= "No imprimir", command=aux2).grid(row=1,column=0,sticky="w",padx=10,pady=10)
    tk.Button(ventana,text= "Imprimir", command=lambda: aux(textPrint)).grid(row=1,column=0,sticky="e",padx=10,pady=10)

    ventana.protocol("WM_DELETE_WINDOW", lambda: retorno.set("False"))
    ventana.wait_variable(retorno)
    ventana.destroy()

    return retorno.get()

def totalizar(apuestas):
    espaciosNum = " "*6
    espaciosLot = " "*13
    totalPrecio = sum(map(lambda x: x.precio,apuestas))
    fecha = datetime.today().strftime("%d/%m/%y")
    apostador = apuestas[0].apostador.nombre + " #" + str(apuestas[0].apostador.id)

    textPrint = f"""------------Quiniela DF------------

Fecha: {fecha}
Jugador: {apostador}

-----------------------------------
Num   Loteria      Turno  Valor
"""

    for apuesta in apuestas:
        textNum = str(apuesta.numero) + espaciosNum[0:len(espaciosNum) - len(str(apuesta.numero))]
        textLot= apuesta.loteria + espaciosLot[0:len(espaciosLot) - len(apuesta.loteria)]
        textTurn = apuesta.turno + "     "
        textValor = f"${apuesta.precio}"
        textPrint+= textNum + textLot + textTurn + textValor + "\n"

    textPrint+= f"""-----------------------------------\n                  Total:  ${totalPrecio}"""
    continuar = windowTicket(textPrint)

    return continuar


def format_right(df):
    numeric_cols = df.select_dtypes(include='number').columns
    right_aligned = {col: 'text-align: right' for col in numeric_cols}
    return df.style.applymap(right_aligned.get, subset=numeric_cols).set_properties(**{'text-align': 'right'})






def obtenerMetricas(df):
    # Creamos un diccionario para almacenar los datos de cada lotería
    data = {}

    # Iteramos por cada lotería
    for loteria in df['loteria'].unique():
        # Filtramos los datos correspondientes a la lotería
        filtro = df[df['loteria'] == loteria].reset_index(drop=True)
        
        # Creamos las columnas de número y precio
        numero_col = loteria + ' numero'
        precio_col = loteria + ' precio'
        
        # Llenamos el diccionario con los datos correspondientes
        data[numero_col] = list(filtro['numero']) + [None] * (len(df) - len(filtro))
        data[precio_col] = list(filtro['precio']) + [None] * (len(df) - len(filtro))

    # Creamos el dataframe resultante a partir del diccionario
    metrica = pd.DataFrame(data)

    # Cambiamos el nombre de las columnas para que sea Nacional Precio - Provincia Precio - Santa Fe Precio...
    isNumero = True
    nameColumns = []
    for columna in metrica.columns:
        if isNumero:
            if len(columna.split(" ")) == 2:
                nameColumns.append(columna.split(" ")[0])
            else:
                nameColumns.append(columna.split(" ")[0] + " " + columna.split(" ")[1])
            isNumero = False
        else:
            nameColumns.append(columna.split(" ")[-1].capitalize())
            isNumero = True

    # Le agregamos un $ a los valores de las columnas Precio
    for columna in metrica:
        if columna.split(" ")[-1].capitalize() == "Precio":
            metrica[columna] = metrica[columna].apply(lambda x: f"${x}" if str(x)!="nan" else x)
    metrica.columns = nameColumns
    return metrica

def condicionesJuegosGanadores(numerosGanadores):
    #Lista para acumular las condiciones
    condiciones = []

    #Recorremos el diccionario con cada loteria y numero, luego consultamos que no este vacio para evitar errores
    for loteria, numero in numerosGanadores.items():
        if numero != '':
            for i in range(4):
                condicion = f"(numero = {numero[i:]} AND loteria = '{loteria}') "
                condiciones.append(condicion)

    # Unir las condiciones con un operador OR
    condiciones = (" OR ".join(condiciones))
    return condiciones


def cerrar(turno,numerosGanadores):
    #Conectamos la base de datos
    conn = sqlite3.connect('LoteDB.db')
    #Hacemos consulta
    query = f"""
        SELECT id, cliente, numero, precio, loteria
        FROM jugadas
        WHERE turno = "{turno}" AND DATE(fecha) = '{datetime.now().date()}' AND vigencia = 1
        ORDER BY cliente ASC, precio DESC, loteria ASC
    """

    #Obtenemos jugadas y metricas
    jugadas = pd.read_sql(query,conn)
    metricas = obtenerMetricas(jugadas)

    #Pasamos los ID a tupla para poder obtenerlos en la consulta y poder actualizar los mismos
    ids_str = ",".join(str(x) for x in list(jugadas["id"].values))
    query = f"""
        UPDATE jugadas SET vigencia = 1
        WHERE id IN ({ids_str})
    """
    executeSQL(query)
    #Agregamos id como indice
    jugadas.set_index("id",inplace=True)
    
    #Le pongo signo $ a la columna precio
    jugadas['precio'] = jugadas['precio'].apply(lambda x: f"${x}" if str(x)!="nan" else x)
    
    #Cambio el nombre de las columnas
    jugadas.columns = ['Cliente','Número','Valor','Lotería']
    
    condiciones = condicionesJuegosGanadores(numerosGanadores)
    query = f"""
        SELECT cliente, numero, precio, loteria
        FROM jugadas
        WHERE ({condiciones}) AND turno = "{turno}" AND DATE(fecha) = '{datetime.now().date()}' AND vigencia = 1
        ORDER BY cliente, precio
    """
    juegosGanadores = pd.read_sql_query(query,conn)

    # Si no hay jugadas, mostramos un mensaje y cerramos la función, si hay jugadas entonces guardamos la información
    if len(jugadas)==0:
        messagebox.showinfo("Atencion","No hay jugadas para realizar el cierre")
        return
    else:
        with pd.ExcelWriter(f"{turno} {datetime.now().date()}.xlsx") as writer:
            metricas.to_excel(writer, sheet_name='Metricas', index=False)
            juegosGanadores.to_excel(writer, sheet_name='Ganadores', index=False)
            jugadas.to_excel(writer, sheet_name='Juegos', index=False)

    conn.close()
    

#cerrar("TM")