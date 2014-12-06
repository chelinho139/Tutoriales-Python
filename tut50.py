#crear una funcion que imprima hola n veces
#recibe n por parametro

def funcion1(n):# forma iteradora
	for x in range(n):
		print "Hola"
		
def funcion2(n): #recursiva
	if n==0:
		return
	print "Hola"
	funcion2(n-1)
