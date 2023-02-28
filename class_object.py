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
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - Deuda: {self.deuda} - Ganancia: {self.ganancia} - Telefono: {self.telefono}"
    
class Jugada:

    def __init__(self,apostador:Cliente,precio:float,loteria:str,pagado:bool,turno:str,numero:int,cobrado=False,vigencia:bool=True,id:str=None):
        self.apostador = apostador
        self.numero = numero
        self.precio = precio
        self.loteria = loteria
        self.fecha = datetime.today()
        self.pagado = pagado
        self.turno = turno
        self.id = id
        self.vigencia = vigencia
        self.cobrado = cobrado
        apostador.jugadas.append(self)

    
    def __str__(self):
        return str(self.precio)
    
    def __repr__(self):
        return str(self.precio)
