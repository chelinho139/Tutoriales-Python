#Chelin Tutorials 2011 All Rights Reserved.
#Cliente Basico
import socket # importo el modulo
print "Tutorial 53 : Cliente"
host = "localhost"
port = 9999
#creo un socket y me conecto
socket1= socket.socket()
socket1.connect((host,port))


oracion= raw_input ("Ingrese una oracion..")

socket1.send(oracion) #mando la oracion
numero=socket1.recv(1024) # recivo el numero de caracteres

print "la oracion ", oracion, "tiene caracteres: ", numero
timepo= raw_input ("presione enter para terminar...")

socket1.close() #cierro el socket