import sqlite3

conexion = sqlite3.connect("Jugadas.db")

conexion.execute(
    """
    CREATE TABLE cliente (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        deuda INTEGER NOT NULL,
        telefono INTEGER
    )
    """
)
conexion.execute(
    """
    CREATE TABLE jugadas (
        id INTEGER PRIMARY KEY,
        cliente TEXT NOT NULL,
        precio INTEGER NOT NULL,
        loteria TEXT NOT NULL,
        fecha DATE,
        pagado BOOLEAN
    )
    """
)


conexion.close()