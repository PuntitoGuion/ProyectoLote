import sqlite3

conexion = sqlite3.connect("LoteDB.db")

conexion.execute(
    """
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        deuda FLOAT NOT NULL,
        telefono TEXT
    );
    """
)

conexion.execute(
    """
    CREATE TABLE jugadas (
        id INTEGER PRIMARY KEY,
        cliente TEXT NOT NULL,
        precio FLOAT NOT NULL,
        loteria TEXT NOT NULL,
        fecha DATE NOT NULL,
        vigencia BOOLEAN NOT NULL,
        cobrado BOOLEAN NOT NULL
    );
    """
)

conexion.close()