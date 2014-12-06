class Punto2D (object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def metodo1(self):
		print "metodo1"
		
class Punto3D (Punto2D):
	def __init__(self,x=0,y=0,z=0):
		Punto2D.__init__(self,x,y)
		self.z=z
		
