#Chelin Tutorials 2011 All Rights Reserved.
#Socket Server Basico
import SocketServer #importo el modulo del server


#creo la clase Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    #se va a llamar en cada coneccion
    def handle(self):
        self.oracion= self.request.recv(1024).strip() #recibo data
        
        self.num = len(self.oracion)# cuento los caracters "1234abc" self.num = 7
        
        print "La oracion recv es ", self.oracion , " el num de chars " , self.num
        self.request.send(str(self.num)) #le mando el numero de caracteres
        
        
def main():
    print "Tutorial 53 Servidores"
    
    host ="localhost" #direccion
    port = 9999
    
    #creo el servidor
    server1 = SocketServer.TCPServer((host,port),MiTcpHandler)
    
    print "server corriendo"
    server1.serve_forever() # ande hasta q cierre el programa

main()
    
    
