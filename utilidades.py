from class_object import *
import sqlite3
import re
from tkinter import messagebox


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
        id = resultado.group(1)
        return id
    messagebox.showerror("Error","Por favor asegurarse de que eligió un jugador de la lista")
    return

def isNumericEntry(value,isFloat=False):
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