import tkinter as tk
from tkinter import ttk, StringVar,IntVar,BooleanVar,DoubleVar,messagebox
from utilidades import *
import random

apuestasTotales = []

def registerValidation():
    if nameRegister.get() !='' and not nameRegister.get().isnumeric():
        nombre = nameRegister.get()
    else:
        messagebox.showerror("Error","Por favor, ingrese el nombre completo")
        return
    try:
        deuda = deudaRegister.get()
    except:
        numero = round(random.uniform(0,999),2)
        messagebox.showerror("Error",f"Por favor ingrese un monto con la deuda actual, por ejemplo: {numero}")
        return
    telefono = telefonoRegister.get()
    registerSQL(nombre,deuda,telefono)

def buscarJugador(event):
    texto = event.widget.get()
    jugadores = [(id,nombre) for id, nombre in id_clients() if texto.lower() in nombre.lower() or texto == str(id)]
    comboBoxGame["values"] = list(map(lambda player: f"{player[1]} ({player[0]})", jugadores))

def gameValidation():
    idApostador = obtenerValorParentesis(playerGame.get())
    loterias = {"Nacional":nacionalGame.get(),"Provincia":provinciaGame.get(),"Santa Fe": santaFeGame.get(),"Cordoba": cordobaGame.get(),"Entre Ríos": entreRiosGame.get(),"Montevideo": montevideoGame.get()}
    turnos = {"TM":turnoManianaGame.get(),"TT":turnoTardeGame.get(),"TN":turnoNocheGame.get()}
    if idApostador == None:
        return
    if not esElMismoApostador(apuestasTotales,idApostador):
        messagebox.showerror("Error",f"Recuerde que esta operando con {apuestasTotales[0].apostador.nombre}. Si desea continuar con otra persona, presione el boton Totalizar para finalizar la operación")
        return
    
    try:
        numero = numGame.get()
    except:
        messagebox.showerror("Error","No se ha ingresado el numero a realizar la apuesta")
        return
    try:
        valor = valorGame.get()
    except:
        messagebox.showerror("Error","No se ha ingresado el valor de la apuesta")
        return
    if not any(loterias):
        messagebox.showerror("Error","No se ha seleccionado ninguna loteria")
        return
    elif not any(turnos.values()):
        messagebox.showerror("Error","No se ha seleccionado turno")
        return
    apuestasTotales.extend(playBets(idApostador,numero,valor,turnos,loterias,pagadoGame.get()))

def gameTotal():
    if len(apuestasTotales)==0:
        messagebox.showerror("Error","No se han ingresado jugadas.")
        return

    continuar = totalizar(apuestasTotales)
    if continuar=="True":
        apuestasTotales.clear()

def closeTurn():
    if turnClose.get() == " ":
        messagebox.showerror("Error","No se ha seleccionado turno.")
        return
    elif not messagebox.askyesno("Atención",f"¿Está seguro que desea cerrar el turno {turnClose.get()}?"):
        return
    cerrar("T" + turnClose.get().upper()[0])


def obtenerNumerosGanadores():
    numerosGanadores = {"Nacional":nacionalClose.get(),"Provincia":provinciaClose.get(),"Santa Fe": santaFeClose.get(),"Cordoba": cordobaClose.get(),"Entre Ríos": entreRiosClose.get(),"Montevideo": montevideoClose.get()}
    validacionEspaciosEnBlanco = map(lambda x: True if x != '' else False, numerosGanadores.values())
    validacionNumeros = map(lambda x: True if len(x)==4 or x=='' else False, numerosGanadores.values())

    #Validamos espacios en blanco, valor de 4 numeros, y que haya seleccionado turno
    if not any(validacionEspaciosEnBlanco):
        messagebox.showerror("Error","Debe ingresar al menos un número de 4 cifras en alguna lotería")
        return
    elif not all(validacionNumeros):
        messagebox.showerror("Error","Recuerde ingresar 4 digitos para la lotería o dejar el espacio en blanco")
        return
    elif turnClose.get() == " ":
        messagebox.showerror("Error","No se ha seleccionado turno.")
        return
    
    if messagebox.askyesno("Atención", f"¿Está seguro que desea obtener los resultados de turno {turnClose.get()}?"):
        reporteGanadores("T" + turnClose.get().upper()[0],numerosGanadores)
    
    #Se vacian los entry de los numeros
    nacionalClose.set('')
    provinciaClose.set('')
    santaFeClose.set('')
    cordobaClose.set('')
    entreRiosClose.set('')
    montevideoClose.set('')
        
# main
mainWindow = tk.Tk()
mainWindow.title("Lote Clan")
#mainWindow.geometry("635x310")
mainWindow.resizable(False,False)
mainWindow.iconbitmap(r".\ico\1.ico")

# crear un objeto Notebook (pestañas)
pestanias = ttk.Notebook(mainWindow)

## crear las pestañas
#tab1 = ttk.Frame(pestanias)
close = ttk.Frame(pestanias)
close2 = ttk.Frame(pestanias)
game = ttk.Frame(pestanias)
clientRegister = ttk.Frame(pestanias)

# agregar pestanias
# el orden en que se agregan es como se van a ver

#pestanias.add(tab1, text="Pestaña 1")
pestanias.add(close, text="Cierre") #3
pestanias.add(game, text="Juego") #1
pestanias.add(clientRegister, text="Registro") #2

# empaquetar las pestanias en la ventana principal
pestanias.pack(fill="both", expand=True)
#Configurar row y columns
configWindows = [game,clientRegister,close,close2]

for window in configWindows:
    for i in range(10):
        window.grid_columnconfigure(i, pad=25)
        window.grid_rowconfigure(i, pad=25)        

#-------------------------------------------------------------------------------------------
# pestania de registro de un cliente
nameRegister = StringVar()
tk.Label(clientRegister,text="Nombre completo: ").grid(row=0,column=0,sticky="w")
nameRegisterEntry = tk.Entry(clientRegister,textvariable=nameRegister,width=20)
nameRegisterEntry.grid(row=0,column=1,sticky="w")

deudaRegister = DoubleVar(value="")
tk.Label(clientRegister,text="Deuda Actual: ").grid(row=1,column=0,sticky="w")
tk.Entry(clientRegister,textvariable=deudaRegister,validate="key",validatecommand=(game.register(isNumericEntryFloat), "%P")).grid(row=1,column=1,sticky="w")

telefonoRegister = StringVar()
tk.Label(clientRegister,text="Teléfono: ").grid(row=2,column=0,sticky="w")
tk.Entry(clientRegister,textvariable=telefonoRegister).grid(row=2,column=1,sticky="w")

tk.Button(clientRegister,command=registerValidation,text="Registrar").grid(row=3,column=1)

#-------------------------------------------------------------------------------------------
# pestania de juego
playerGame = StringVar()
tk.Label(game,text="Jugador: ").grid(row=0,column=0,sticky="w")
comboBoxGame = ttk.Combobox(game,textvariable=playerGame,width=17)
comboBoxGame["values"] = list(map(lambda player: f"{player[1]} ({player[0]})", id_clients()))
comboBoxGame.bind("<KeyRelease>", buscarJugador)
comboBoxGame.grid(row=0,column=1,sticky="w")

numGame = IntVar(value="")
tk.Label(game,text="Número: ").grid(row=1,column=0,sticky="w")
tk.Entry(game,textvariable=numGame,validate="key",validatecommand=(game.register(isNumericEntry), '%S')).grid(row=1,column=1,sticky="w")

valorGame = DoubleVar(value="")
tk.Label(game,text="Valor: ").grid(row=2,column=0,sticky="w")
tk.Entry(game,textvariable=valorGame,validate="key",validatecommand=(game.register(isNumericEntryFloat), "%P")).grid(row=2,column=1,sticky="w")

nacionalGame = BooleanVar()
tk.Checkbutton(game,text="Nacional",variable=nacionalGame).grid(row=0,column=2,sticky="w")
provinciaGame = BooleanVar()
tk.Checkbutton(game,text="Provincia",variable=provinciaGame).grid(row=0,column=3,sticky="w")
santaFeGame = BooleanVar()
tk.Checkbutton(game,text="Santa Fe",variable=santaFeGame).grid(row=1,column=2,sticky="w")
cordobaGame = BooleanVar()
tk.Checkbutton(game,text="Cordoba",variable=cordobaGame).grid(row=1,column=3,sticky="w")
entreRiosGame = BooleanVar()
tk.Checkbutton(game,text="Entre Rios",variable=entreRiosGame).grid(row=2,column=2,sticky="w")
montevideoGame = BooleanVar()
tk.Checkbutton(game,text="Montevideo",variable=montevideoGame).grid(row=2,column=3,sticky="w")

tk.Label(game,text="Paga: ").grid(row=3,column=0,sticky="w")
pagadoGame = BooleanVar(value=True)
tk.Radiobutton(game,text="Si",variable=pagadoGame,value=True).grid(row=3,column=1,sticky="w")
tk.Radiobutton(game,text="No",variable=pagadoGame,value=False).grid(row=3,column=1)

turnoManianaGame = BooleanVar()
tk.Checkbutton(game,text="Turno Mañana",variable=turnoManianaGame).grid(row=0,column=4,sticky="w")
turnoTardeGame = BooleanVar()
tk.Checkbutton(game,text="Turno Tarde",variable=turnoTardeGame).grid(row=1,column=4,sticky="w")
turnoNocheGame = BooleanVar()
tk.Checkbutton(game,text="Turno Noche",variable=turnoNocheGame).grid(row=2,column=4,sticky="w")

tk.Button(game, text="Sumar",command=gameValidation).grid(row=9,column=1)
tk.Button(game, text="Totalizar",command=gameTotal).grid(row=9,column=2)

#-------------------------------------------------------------------------------------------
# pestania cierre

turnClose = StringVar(value=" ")
tk.Label(close,text="Seleccione Turno: ",).grid(row=0,column=3,sticky="w")
tk.Radiobutton(close,text="Turno Mañana",variable=turnClose,value="mañana").grid(row=0,column=4,sticky="w")
tk.Radiobutton(close,text="Turno Tarde",variable=turnClose,value="tarde").grid(row=1,column=4,sticky="w")
tk.Radiobutton(close,text="Turno Noche",variable=turnClose,value="noche").grid(row=2,column=4,sticky="w")

ttk.Separator(close, orient='vertical').grid(row=0, column=2, rowspan=8, sticky='ns', padx=10, pady=10)

nacionalClose = StringVar()
tk.Label(close, text="Nacional: ").grid(row=0,column=0,sticky="w")
tk.Entry(close,textvariable=nacionalClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=0,column=1,sticky="w")

provinciaClose = StringVar()
tk.Label(close, text="Provincia: ").grid(row=1,column=0,sticky="w")
tk.Entry(close,textvariable=provinciaClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=1,column=1,sticky="w")

santaFeClose = StringVar()
tk.Label(close, text="Santa Fe: ").grid(row=2,column=0,sticky="w")
tk.Entry(close,textvariable=santaFeClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=2,column=1,sticky="w")

entreRiosClose = StringVar()
tk.Label(close, text="Entre Ríos: ").grid(row=3,column=0,sticky="w")
tk.Entry(close,textvariable=entreRiosClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=3,column=1,sticky="w")

cordobaClose = StringVar()
tk.Label(close, text="Cordoba: ").grid(row=4,column=0,sticky="w")
tk.Entry(close,textvariable=cordobaClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=4,column=1,sticky="w")

montevideoClose = StringVar()
tk.Label(close, text="Montevideo: ").grid(row=5,column=0,sticky="w")
tk.Entry(close,textvariable=montevideoClose,validate="key",validatecommand=(close.register(isNumericEntry), '%S')).grid(row=5,column=1,sticky="w")

tk.Button(close,text="Cerrar turno",command=closeTurn).grid(row=6,column=4,sticky="e")

tk.Button(close,text="Generar ganadores",command=obtenerNumerosGanadores).grid(row=6,column=1,sticky="w")

mainWindow.mainloop()