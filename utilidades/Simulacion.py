#!/usr/bin/env python
# Título: 
# Autor: Kevin Rivera
# Descripción:
from .Arreglo import Arreglo
from queue import Queue

class  Simulacion():


    def __init__(self):
        '''Inicializando los datos de la simulacion'''
        print("Inicializando...")
        self.masterClock = 0
        # 0 Significa Oscioso, 1 para Ocupado
        self.mecanico = 0
        # Lleva el control de ocurrencia de un evento
        self.evento = False
        # Las primeras tres posiciones son las maquinas, la ultima el reloj de salida
        self.vector = Arreglo(1, 4, 9, 8000)
        # Indice de de la posicion con el menor valor
        self.indice = 0
        # Numero de clientes en cola
        self.n = 0
        #Inicializar cola
        self.cola = Queue()

    def llegada(self):
        print("Ha ocurrido una llegada")
        self.masterClock = self.vector.getValue(self.indice)

        if self.n == 0:
            self.mecanico = 1
            self.vector.setValue(self.vector.longitud()-1,self.masterClock +5)
            self.n=1
            self.vector.setValue(self.indice,'REPARACION')
        else:
            self.n += 1
            self.cola.put(self.indice)
            self.vector.setValue(self.indice,'EN ESPERA')


    def salida(self):
        print("Ha ocurrido una salida")
        self.masterClock = self.vector.getValue(self.vector.longitud()-1)
        self.vector.setValue(self.vector.devolverIndiceElemento('REPARACION'),self.masterClock +10)
        self.n -= 1
        if self.n == 0:
            self.mecanico = 0
        else:
            self.vector.setValue(self.cola.get(),'REPARACION')
            self.vector.setValue(self.vector.longitud()-1,self.masterClock + 5)



    def simular(self):
        self.evento = False
        self.indice = self.vector.encontrarMinimo()
        temporal = self.vector.getValue(self.indice)
        if self.masterClock == self.vector.getValue(self.indice):
            self.evento = True
            if self.vector.getValue(self.vector.longitud() -1) == self.vector.getValue(self.indice):
                self.salida()
            else:
                self.llegada()

        if self.evento:
            while self.vector.includes(temporal):
                if self.vector.indexOf(temporal) == self.vector.longitud()-1:
                    self.salida()
                else:
                    self.llegada()

        #TODO Imprimir estado de las variables
        self.masterClock += 1

    def imprimirIteracion(self):
        estado = "=======================================================================================\n"
        estado += "Master Clock: " + str(self.masterClock) + " Mecanico: " + str(self.mecanico)
        estado += "=======================================================================================\n"
        print(estado)
        self.vector.imprimir()


