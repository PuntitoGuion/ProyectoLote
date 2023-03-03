# import tkinter as tk
# from utilidades import executeSQL

# executeSQL("""
#     DELETE FROM jugadas
# """)


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

# Crear el separador
separator = ttk.Separator(frame, orient='vertical')
separator.pack(side='left', fill='y', padx=10, pady=10)

# Agregar widgets a la primera sección del Frame
label1 = tk.Label(frame, text="Sección 1")
label1.pack(side='left', padx=10, pady=10)

# Crear el separador
separator = ttk.Separator(frame, orient='vertical')
separator.pack(side='left', fill='y', padx=10, pady=10)

# Agregar widgets a la segunda sección del Frame
label2 = tk.Label(frame, text="Sección 2")
label2.pack(side='left', padx=10, pady=10)

root.mainloop()
