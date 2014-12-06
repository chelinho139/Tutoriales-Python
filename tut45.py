def f2():
	try:
		a=55
	except IOError:
		print "IOError ecnontrado"
	except ZeroDivisionError:
		print "No se puede dividir por 0"
	except ValueError:
		print "Se encontro un error"
		a=23
		print "a:",a
	except:
		print "se encontro un error de tipo desconocido"
	finally:
		print "Cerrando archivo"
		a=0
		print a
			
