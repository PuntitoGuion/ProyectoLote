from class_object import *
import sqlite3


def executeSQL(query:str,datos:tuple):
    conn = sqlite3.connect('LoteDB.db')
    cursor = conn.cursor()
    cursor.execute(query, datos)
    conn.commit()
    conn.close()


def registerSQL(nombre,deuda,telefono):
    cliente = Cliente(nombre,deuda,telefono)
    query = 'INSERT INTO clientes (nombre, deuda, telefono) VALUES (?, ?, ?)'
    datos = (str(cliente.nombre),float(cliente.deuda),str(cliente.telefono))
    executeSQL(query,datos)