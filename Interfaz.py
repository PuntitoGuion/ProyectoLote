import tkinter as tk
from tkinter import ttk, StringVar,IntVar,BooleanVar,DoubleVar,messagebox
from utilidades import *


def registerValidation():
    if nameRegister.get() !='' and not nameRegister.get().isnumeric():
        nombre = nameRegister.get()
    else:
        messagebox.showerror("Error","Por favor, ingrese el nombre completo")
        return
    try:
        deuda = deudaRegister.get()
    except:
        messagebox.showerror("Error","Por favor ingrese un monto con la deuda actual, por ejemplo: 14.5")
        return
    telefono = telefonoRegister.get()
    registerSQL(nombre,deuda,telefono)

def buscarJugador(event):
    texto = event.widget.get()
    jugadores = [(id,nombre) for id, nombre in id_clients() if texto.lower() in nombre.lower() or texto == str(id)]
    comboBoxGame["values"] = list(map(lambda player: f"{player[1]} ({player[0]})", jugadores))


# main
mainWindow = tk.Tk()
mainWindow.title("Lote Clan")
mainWindow.geometry("1280x720")
mainWindow.resizable(False,False)
mainWindow.

# crear un objeto Notebook (pestañas)
pestanias = ttk.Notebook(mainWindow)

## crear las pestañas
#tab1 = ttk.Frame(pestanias)
#tab2 = ttk.Frame(pestanias)
game = ttk.Frame(pestanias)
clientRegister = ttk.Frame(pestanias)

## agregar pestanias
#pestanias.add(tab1, text="Pestaña 1")
#pestanias.add(tab2, text="Pestaña 2")
pestanias.add(game, text="Juego")
pestanias.add(clientRegister, text="Registro")

# empaquetar las pestanias en la ventana principal
pestanias.pack(fill="both", expand=True)
#Configurar row y columns
for i in range(10):
    game.grid_columnconfigure(i, pad=25)
    game.grid_rowconfigure(i, pad=25)
for i in range(10):
    clientRegister.grid_columnconfigure(i, pad=25)
    clientRegister.grid_rowconfigure(i, pad=25)
#-------------------------------------------------------------------------------------------
# pestania de registro de un cliente
nameRegister = StringVar()
tk.Label(clientRegister,text="Nombre completo: ").grid(row=0,column=0,sticky="w")
tk.Entry(clientRegister,textvariable=nameRegister,width=20).grid(row=0,column=1,sticky="w")

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

#tk.Label(game,text="Teléfono: ").grid(row=3,column=0,padx=15,pady=15)
#tk.Entry(game,textvariable=telefonoRegister).grid(row=3,column=1)

tk.Button(game, text="Test",command=lambda: obtenerValorParentesis(playerGame.get())).grid(row=4,column=1)

mainWindow.mainloop()
