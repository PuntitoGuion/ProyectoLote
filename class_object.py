from datetime import datetime

class Cliente:
    jugadas = []

    def __init__(self,nombre:str,deuda:float=0,ganancia:float=0,telefono:str=None,id:str=None):
        self.nombre = nombre
        self.telefono = telefono
        self.deuda = deuda
        self.id = id
        self.ganancia = ganancia

    def debe(self):
        return sum(jugada.precio for jugada in filter(lambda x: x.pagado,self.jugadas))

class Jugada:

    def __init__(self,apostador:Cliente,precio:float,loteria:str,pagado:bool,turno:str):
        self.apostador = apostador
        self.precio = precio
        self.loteria = loteria
        self.fecha = datetime.today()
        self.pagado = pagado
        self.turno = turno
        apostador.jugadas.append(self)

    
    def __str__(self):
        return str(self.precio)
    
    def __repr__(self):
        return str(self.precio)

cliente1 = Cliente("Julián Ferrari","+541157595519")

listaJugadas = (Jugada(cliente1,15,"Provincia",True,"TM"),
                Jugada(cliente1,32,"Nacional",True,"TT"),
                Jugada(cliente1,45,"Entre Rios",False,"TN"),
                Jugada(cliente1,22,"A",True,"TM"),
                Jugada(cliente1,35,"B",False,"TT")
                )

prueba = Jugada(cliente1,20,"Provincia",False,"TN")