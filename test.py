import sqlite3

# conectarse a la base de datos
conn = sqlite3.connect('LoteDB.db')

import sqlite3

# conectarse a la base de datos
conn = sqlite3.connect('LoteDB.db')

# crear un cursor
cursor = conn.cursor()

# definir los valores para el nuevo registro
nuevo_id = 1
nuevo_nombre = 'Juan'
deuda = 30
telefono = 541157595519

# ejecutar la sentencia SQL para insertar el nuevo registro
cursor.execute('INSERT INTO clientes (nombre, deuda, telefono) VALUES (?, ?, ?)', ("Marcela Luquez", 54.50, "+541124982929"))

# confirmar los cambios en la base de datos
conn.commit()

# cerrar la conexión a la base de datos
conn.close()


# import tkinter as tk
# from tkinter import ttk

# # crear una ventana principal
# root = tk.Tk()
# root.title("Mi ventana con pestañas")
# root.geometry("1280x720")

# # crear un objeto Notebook (pestañas)
# notebook = ttk.Notebook(root)

# # crear las pestañas
# tab1 = ttk.Frame(notebook)
# tab2 = ttk.Frame(notebook)
# tab3 = ttk.Frame(notebook)
# tab4 = ttk.Frame(notebook)

# # agregar las pestañas al Notebook
# notebook.add(tab1, text="Pestaña 1")
# notebook.add(tab2, text="Pestaña 2")
# notebook.add(tab3, text="Pestaña 3")
# notebook.add(tab4, text="Pestaña 4")

# # agregar contenido a cada pestaña
# tk.Label(tab1, text="Contenido de la pestaña 1").pack(padx=20, pady=20)
# tk.Label(tab2, text="Contenido de la pestaña 2").pack(padx=20, pady=20)
# tk.Label(tab3, text="Contenido de la pestaña 3").pack(padx=20, pady=20)
# tk.Label(tab4, text="Contenido de la pestaña 4").pack(padx=20, pady=20)

# # empaquetar el Notebook en la ventana principal
# notebook.pack(fill="both", expand=True)

# # iniciar el bucle principal de la aplicación
# root.mainloop()
