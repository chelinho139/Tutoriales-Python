import socket

#va a mandar mensajes al servidor

def main():
    print "Cliente 1.0"
    
    msj =""
    host, port = "localhost" , 9999
    #creo un socket y me conecto
    sock= socket.socket()
    sock.connect((host,port))
    
    print "Ingrese un mensaje o salir para terminar"
    while msj != "salir":
        msj = raw_input ("Usted dice: ")
        #intento mandar msj
        try:
            sock.send(msj)
        # si no se puede entonces salgo
        except:
            print "no se mando el mensaje"
            msj="salir"
        
    sock.close() #recuerden cerrar el socket

main()