import tkinter as tk
from tkinter import ttk, StringVar,IntVar,BooleanVar,DoubleVar
from utilidades import *


def test():
    print(nameRegister.get())
    print(deudaRegister.get())
    print(telefonoRegister.get())

# main
mainWindow = tk.Tk()
mainWindow.title("Lote Clan")
mainWindow.geometry("1280x720")
mainWindow.resizable(False,False)

# crear un objeto Notebook (pestañas)
pestanias = ttk.Notebook(mainWindow)

## crear las pestañas
#tab1 = ttk.Frame(pestanias)
#tab2 = ttk.Frame(pestanias)
#tab3 = ttk.Frame(pestanias)
clientRegister = ttk.Frame(pestanias)

## agregar pestanias
#pestanias.add(tab1, text="Pestaña 1")
#pestanias.add(tab2, text="Pestaña 2")
#pestanias.add(tab3, text="Pestaña 3")
pestanias.add(clientRegister, text="Registrar")

# empaquetar las pestanias en la ventana principal
pestanias.pack(fill="both", expand=True)

# pestania de registro de un cliente
nameRegister = StringVar()
tk.Label(clientRegister,text="Nombre completo: ").grid(row=0,column=0,padx=15,pady=15)
tk.Entry(clientRegister,textvariable=nameRegister).grid(row=0,column=1)

deudaRegister = DoubleVar()
deudaRegister.set(0)
tk.Label(clientRegister,text="Deuda Actual: ").grid(row=1,column=0,padx=15,pady=15)
tk.Entry(clientRegister,textvariable=deudaRegister).grid(row=1,column=1)

telefonoRegister = StringVar()
tk.Label(clientRegister,text="Teléfono: ").grid(row=2,column=0,padx=15,pady=15)
tk.Entry(clientRegister,textvariable=telefonoRegister).grid(row=2,column=1)

tk.Button(clientRegister,command=lambda: registerSQL(nameRegister.get(),deudaRegister.get(),telefonoRegister.get())).grid(row=3,column=3,padx=15,pady=15)



mainWindow.mainloop()
