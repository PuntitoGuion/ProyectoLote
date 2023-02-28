# import sqlite3

# conn = sqlite3.connect('LoteDB.db')
# cursor = conn.cursor()
# cursor.execute('INSERT INTO clientes (nombre, deuda, telefono, ganancia) VALUES (?, ?, ?, ?)', ("Debora Ferrari", 55.50, "+3432452332", 32))
# conn.commit()
# conn.close()

import tkinter as tk

def on_enter_press(event):
    btn.invoke()

def button_command():
    print("El botón ha sido presionado")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Presionar", command=button_command)
btn.pack()

entry.bind("<Return>", on_enter_press)

root.mainloop()
