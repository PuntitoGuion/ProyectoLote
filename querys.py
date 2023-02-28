import sqlite3

conexion = sqlite3.connect("LoteDB.db")

conexion.execute(
    """
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        deuda FLOAT NOT NULL,
        ganancia FLOAT NOT NULL,
        telefono TEXT
    );
    """
)

conexion.execute(
    """
    CREATE TABLE jugadas (
        id INTEGER PRIMARY KEY,
        cliente TEXT NOT NULL,
        numero INTEGER NOT NULL,
        precio FLOAT NOT NULL,
        loteria TEXT NOT NULL,
        turno TEXT NOT NULL,
        fecha DATE NOT NULL,
        vigencia INTEGER NOT NULL,
        pago INTEGER NOT NULL,
        cobrado INTEGER NOT NULL
    );
    """
)

conexion.close()