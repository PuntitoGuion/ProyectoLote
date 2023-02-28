# import sqlite3

# conn = sqlite3.connect('LoteDB.db')
# cursor = conn.cursor()
# cursor.execute('INSERT INTO clientes (nombre, deuda, telefono, ganancia) VALUES (?, ?, ?, ?)', ("Debora Ferrari", 55.50, "+3432452332", 32))
# conn.commit()
# conn.close()

import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo Checkbutton con texto justificado a la izquierda")

# Crear un LabelFrame que contenga el Checkbutton
label_frame = tk.LabelFrame(root, padx=10, pady=10, labelanchor="w")
label_frame.pack(padx=10, pady=10)

# Crear el Checkbutton y vincularlo al LabelFrame
checkbutton = tk.Checkbutton(label_frame, text="Opciódasn 1").pack(padx=10, pady=10,anchor="w")
checkbutton = tk.Checkbutton(label_frame, text="Opción dasad1").pack(padx=10, pady=10,anchor="w")
checkbutton = tk.Checkbutton(label_frame, text="Opcióasdsn 1").pack(padx=10, pady=10,anchor="w")
checkbutton = tk.Checkbutton(label_frame, text="Opci213ón 1").pack(padx=10, pady=10,anchor="w")

# Ejecutar el loop principal de la aplicación
root.mainloop()
