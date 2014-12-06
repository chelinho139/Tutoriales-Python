#Chelin Tutorials 2011 All Rights Reserved.
#http://chelintutorials.blogspot.com/
#Threads

import time
import thread #imporar el modulo

#funcion que voy a colocar en thread
def imprimir_mensaje(mensaje):
    while True:
        print(mensaje)
        time.sleep(1)


def main():
    mensaje="Thread1" #variable aux
    mensaje2="Thread2" #variable aux
    
    #empiezo el thread
    thread.start_new_thread(imprimir_mensaje, (mensaje,))

    #empiezo otro thread
    thread.start_new_thread(imprimir_mensaje, (mensaje2,))

    
    x = raw_input("Estoy esperando q presiones enter...\n")
    
    print("Termino la funcion main")
    #se cerraran las threads activas de esta funcion.
    
main()
