class Guerrero(object):
	def __init__(self,nombre="Guerrero"):
		self.hp=100
		self.mp=20
		self.nombre=nombre
	
	def atacar(self):
		print "el jugador ", self.nombre ,"ataco"
		
class Elfo(Guerrero):
	def __init__(self,nombre="Elfo"):
		Guerrero.__init__(self,nombre)
		self.flechas=10
	def arco(self):
		print "El elfo ataco con su arco"
		self.flechas-=1
		self.flechas-=1

class Humano(Guerrero):
	def __init__(self,nombre="Humano"):s
		Guerrero.__init__(self,nombre)
		self.estado_escudo=100
	
	def bloquiar(self):
		print "Se bloquio el ataque"
		self.estado_escudo-=20


