from datetime import datetime

class Cliente:
    jugadas = []

    def __init__(self,nombre:str,telefono):
        self.nombre = nombre
        self.telefono = telefono

    def debe(self):
        return sum(jugada.precio for jugada in filter(lambda x: x.pagado,self.jugadas))

class Jugada:

    def __init__(self,apostador:Cliente,precio:float,loteria:str,pagado:bool):
        self.apostador = apostador
        self.precio = precio
        self.loteria = loteria
        self.fecha = datetime.today().strftime("%d/%m/%y")
        self.pagado = pagado
        apostador.jugadas.append(self)
    
    def __str__(self):
        return str(self.precio)
    
    def __repr__(self):
        return str(self.precio)

cliente1 = Cliente("Julián Ferrari","+541157595519")

listaJugadas = (Jugada(cliente1,15,"Provincia",True),
                Jugada(cliente1,32,"Nacional",True),
                Jugada(cliente1,45,"Entre Rios",False),
                Jugada(cliente1,22,"A",True),
                Jugada(cliente1,35,"B",False)
                )

prueba = Jugada(cliente1,20,"Provincia",False)