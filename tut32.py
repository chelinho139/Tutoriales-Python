#03
import random

class Jugador(object):
    def __init__(self, nombre="Jugador" ):
        self.nombre= nombre
        self.hp_max=random.randrange(45,55)
        self.mp_max=random.randrange(40,50)
        self.fuerza=random.randrange(3,7)
        self.inteligencia=random.randrange(2,5)
        self.hp=self.hp_max
        self.mp=self.mp_max
        self.habilidades=[Bola_de_fuego(),Golpe_letal(),Golpiar()]
    def __str__(self):
        return str(self.nombre)+" HP" +str(self.hp_max)+"/"+str(self.hp)

    def stats(self):
        print self.nombre
        print "Hp: ",self.hp_max,"(max) / ",self.hp
        print "Mp: ",self.mp_max, "(max)/ ", self.mp
        print "Fuerza:",self.fuerza
        print "Inteligencia:",self.inteligencia

    def eleccion(self):
        print "Elija una habilidad"
        print "0-Bola de fuego **10mp"
        print "1-Golpe Letal **5mp"
        print "2-Golpiar **no requiere mp)"
        x= input("? ")
        return x

class AI(object):
     def __init__(self):
        self.hp_max=random.randrange(45,55)
        self.mp_max=random.randrange(40,50)
        self.fuerza=random.randrange(3,7)
        self.inteligencia=random.randrange(2,5)
        self.hp=self.hp_max
        self.mp=self.mp_max
        self.habilidades=[Bola_de_fuego(),Golpe_letal(),Golpiar()]
     def __str__(self):
        return "AI: " + " HP" +str(self.hp_max)+"/"+str(self.hp)
     def stats(self):
        print "Hp: ",self.hp_max,"(max) / ",self.hp
        print "Mp: ",self.mp_max, "(max)/ ", self.mp
        print "Fuerza",self.fuerza
        print "Inteligencia",self.inteligencia
     def eleccion(self):
         x=random.randrange(0,3)
         return x

class Bola_de_fuego(object):
    def __init__(self):
        self.dano=0
        self.nombre="BOLA DE FUEGO"
    def devolver_ataque(self,origen):
        if origen.mp<10:
            return 0
        else:
            self.dano=random.randrange(13,19)+origen.inteligencia
            origen.mp+= -10
            return self.dano


class Golpe_letal(object):
    def __init__(self):
        self.nombre="GOLPE LETAL"
        self.dano=0
    def devolver_ataque(self,origen):
        if origen.mp<5:
            return 0
        else:
            self.dano=random.randrange(7,15)+origen.fuerza
            origen.mp-=5
            return self.dano


class Golpiar(object):
    def __init__(self):
        self.nombre="Golpiar"
        self.dano=0
    def devolver_ataque(self,origen):
        self.dano=origen.fuerza+origen.inteligencia
        return self.dano






def main():
    print " BIENVENIDOS A CHELINGAME\n"
    print "Modo de juego"
    print "1-Single Player"
    print "2-Multiplayer"
    modo=input("? ")
    if modo==1:
        j2=AI()

    if modo==2:
        print "ingrese su nombre j2"
        name=raw_input("? ")
        j2=Jugador(name)

    print "ingrese su nombre j1"
    name=raw_input("? ")
    j1=Jugador(name)
    print"STATS J1"
    j1.stats()
    tiempo=raw_input("..,.")
    print "STATS J2"
    j2.stats()
    tiempo=raw_input(".....")
    while j1.hp>0 and j2.hp>0:

        print "Turno J1"
        print j1
        print "mp",j1.mp
        print j2
        elec1=j1.eleccion()
        print "Se utilizo la hablidad",j1.habilidades[elec1].nombre
        dano1=j1.habilidades[elec1].devolver_ataque(j1)
        print "dano efectuado",dano1
        j2.hp-=dano1
        if j1.hp<=0 or j2.hp<=0:
            break
        tiempo=raw_input(".....")
        print "...."
        print "Turno J2"
        print j1
        print j2
        print "mp",j2.mp
        elec2=j2.eleccion()
        print "Se utilizo la hablidad",j2.habilidades[elec2].nombre
        dano2=j2.habilidades[elec2].devolver_ataque(j2)
        print "dano efectuado",dano2
        j1.hp-=dano2
        tiempo=raw_input(".....")
    if j1.hp>0:
        print "Gano j1"
    else:
        print "Gano j2"

main()
