from class_object import *
import sqlite3
import pandas as pd


def executeSQL(query:str,datos:tuple=()):
    conn = sqlite3.connect('LoteDB.db')
    cursor = conn.cursor()
    cursor.execute(query, datos)
    registros = cursor.fetchall()
    conn.commit()
    conn.close()
    return registros


def registerSQL(nombre,deuda,telefono):
    cliente = Cliente(nombre,deuda,telefono)
    query = 'INSERT INTO clientes (nombre, deuda, telefono) VALUES (?, ?, ?)'
    datos = (str(cliente.nombre),float(cliente.deuda),str(cliente.telefono))
    executeSQL(query,datos)

def id_client():
    unaQuery = """
        SELECT *
        FROM clientes
    """
    registros = executeSQL(unaQuery)

    clientesID = {'id':[],'nombre':[]}
    #clientesID = {}
    for registro in registros:
        clientesID['id'].append(registro[0]) # diccionario donde la clave id y nombre tiene como valor una lista de los registros
        clientesID['nombre'].append(registro[1])

        #clientesID[registro[0]] = registro[1]   -- Diccionario donde cada clave y valor es un registro
    registrodf = pd.DataFrame(clientesID)
    print(registrodf)