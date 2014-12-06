def primera():
	x=5
	print x
	segunda(x)
	print x
	print "Volvi a primera"

def segunda(a):
	a+=2
	print a
	tercera(a)
	print "Volvi a segunda"
	
def tercera(b):
	b+=1
	print b
	

def prim():
	x=5
	seg(x)
	print x

def seg(a):
	a=4

