
def cuadradoentero():
	print "Ingrese un numero entero positivo"
	
	while True:
		try:
			x=raw_input("? ")
			x=int(x)
			if x<1:
				raise ValueError, "ingrese un numero mayor a 0"
			break
		except: 
			print "Ingrese un numero entero mayor a 0"
			
	print x*x
	
	

	
