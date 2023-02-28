from class_object import *
import sqlite3
import re
from tkinter import messagebox
import time
from functools import reduce

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

def obtenerLoterias(loteriasBool):
    loterias = []
    if loteriasBool[0]:
        loterias.append("Nacional")
    if loteriasBool[1]:
        loterias.append("Provincia")
    if loteriasBool[2]:
        loterias.append("Santa Fe")
    if loteriasBool[3]:
        loterias.append("Cordoba")
    if loteriasBool[4]:
        loterias.append("Entre Ríos")
    if loteriasBool[5]:
        loterias.append("Montevideo")

    return loterias

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

    for turno,suValor in turnos.items():
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
    

cliente1 = Cliente("Julian Ferrari",10,0,"+541157595519",10)

cliente2 = Cliente("Marta Bergara",22,23,"+541148425232",5)


unaApuesta = Jugada(cliente1,10,"Cordoba",True,"TM",10,True)

otraApuesta = Jugada(cliente2,4,"Entre Ríos",True,"TN",5,True)

listaDeApuestas = [otraApuesta,unaApuesta,unaApuesta,unaApuesta,unaApuesta,unaApuesta]

#print(verificarMismoApostador(listaDeApuestas))