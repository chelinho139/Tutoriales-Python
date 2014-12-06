class Auto(object):
	
	def __init__(self,color="Sin color",marca="Sin marca",prendido=False):
		self.color=color
		self.marca=marca
		self.estaprendido=prendido
	
	def __str__(self):
		if self.estaprendido:
				estado="Prendido"
		else:
				estado="Apagado"
		return "El auto "+str(self.marca)+" de color "+str(self.color)+"esta "+str(estado)

	
	def arrancar(self):
		if self.estaprendido:
			print "El auto ya esta prendido"
		else:
			self.estaprendido=True
			print "El auto arranco"
			

			
