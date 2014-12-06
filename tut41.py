class Pila(object):
	def __init__(self):
		self.items=[]
		
	def apilar(self, dato):
		self.items.append(dato)
		
	def desapilar(self):
		if self.esta_vacia():
			return None
		else:
			return self.items.pop()
			
	def esta_vacia(self):
		if len(self.items)==0:
			return True
		else:
			return False

class Cola(object):

	def __init__(self):
		self.items=[]
		
	def encolar(self,x):
		self.items.append(x)
	
	def esta_vacia(self):
		if len(self.items)==0:
			return True
		else:
			return False
			
	def desencolar(self):
		if self.esta_vacia():
			return None
		else:
			return self.items.pop(0)		

def recepcion():
	cola1=Cola()
	print "Bienvenido"
	while True:
		print "1-Agregar Nuevo Paciente"
		print "2-Llamar al prox Paciente"
		print "3-Cantidad de pacientes"
		print "4-salir"
		x=raw_input(" ?")
		x=int(x)
		if x==1:
			paciente=raw_input("nombre del paciente? ")
			cola1.encolar(paciente)
		elif x==2:
			print cola1.desencolar()
		elif x==3:
			print len(cola1.items)
		elif x==4:
			break
		else:
			print "ingrese una opcion valida"
				
recepcion()
