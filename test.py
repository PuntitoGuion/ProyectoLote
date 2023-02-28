# import sqlite3

# conn = sqlite3.connect('LoteDB.db')
# cursor = conn.cursor()
# cursor.execute('INSERT INTO clientes (nombre, deuda, telefono, ganancia) VALUES (?, ?, ?, ?)', ("Debora Ferrari", 55.50, "+3432452332", 32))
# conn.commit()
# conn.close()

import tkinter as tk
from utilidades import executeSQL

executeSQL("""
    DELETE FROM jugadas
""")
