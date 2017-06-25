#!/usr/bin/env python
# Título: 
# Autor: Kevin Rivera
# Descripción:
from .Arreglo import Arreglo
from queue import Queue
import random

class  Simulacion():


    def __init__(self,iteraciones):
        '''Inicializando los datos de la simulacion'''
        print("Inicializando...")
        self.masterClock = 0
        # 0 Significa Oscioso, 1 para Ocupado
        self.mecanico = 0
        # Lleva el control de ocurrencia de un evento
        self.evento = False
        # Las primeras 6 posiciones son las maquinas, la ultima el reloj de salida
        self.vector = Arreglo(int(random.uniform(0,iteraciones)),
                              int(random.uniform(0,iteraciones)),
                              int(random.uniform(0,iteraciones)),
                              int(random.uniform(0,iteraciones)),
                              int(random.uniform(0,iteraciones)),
                              int(random.uniform(0,iteraciones)),
                              iteraciones+1)
        # Indice de de la posicion con el menor valor
        self.indice = 0
        # Numero de clientes en cola
        self.n = 0
        #Inicializar cola
        self.cola = Queue()
        #Numero de iteraciones
        self.iteraciones = iteraciones

    def llegada(self):
        print("Ha ocurrido una llegada")
        self.masterClock = self.vector.getValue(self.vector.encontrarMinimo())


        if self.n == 0:
            self.mecanico = 1
            self.vector.setValue(self.vector.longitud() - 1, int(random.uniform(self.masterClock,
                                                                                self.iteraciones)))
            self.n=1
            self.vector.setValue(self.vector.encontrarMinimo(),'R')
        else:
            self.n += 1
            self.cola.put(self.vector.encontrarMinimo())
            self.vector.setValue(self.vector.encontrarMinimo(),'E')


    def salida(self):
        print("Ha ocurrido una salida")
        self.masterClock = self.vector.getValue(self.vector.longitud()-1)
        self.vector.setValue(self.vector.devolverIndiceElemento('R'),
                             int(random.uniform(self.masterClock,self.iteraciones)))
        self.n -= 1
        if self.n == 0:
            self.mecanico = 0

        else:
            self.vector.setValue(self.cola.get(),'R')

        self.vector.setValue(self.vector.longitud() - 1,
                             int(random.uniform(self.masterClock+1,self.iteraciones)))

    def simular(self):

        self.encabezado()
        print("Condiciones iniciales: ")
        self.vector.imprimir()
        while self.masterClock < self.iteraciones:
            self.evento = False
            self.indice = self.vector.encontrarMinimo()
            temporal = self.vector.getValue(self.indice)
            #print("Indice: " + str(self.indice) + " temporal: " + str(temporal) + " \n")
            if self.masterClock == self.vector.getValue(self.indice):
                self.evento = True
                if self.vector.getValue(self.vector.longitud() -1) == self.vector.getValue(self.indice):
                    self.salida()
                else:
                    self.llegada()

            if self.evento:
                while self.vector.includes(temporal) and self.masterClock < self.iteraciones:
                    if self.vector.indexOf(temporal) == self.vector.longitud()-1:
                        self.salida()
                    else:
                        self.llegada()



            self.imprimirIteracion()
            self.masterClock += 1

    def imprimirIteracion(self):

        estado = "=======================================================================================\n"
        estado += "Master Clock: " + str(self.masterClock) + " Mecanico: " + str(self.mecanico) +"\n"
        estado += "=======================================================================================\n"
        print(estado)
        self.vector.imprimir()

    def encabezado(self):
        linea = "------------------------------------------------------------------------------------\n"
        linea += "                            UNIVERSIDAD DE EL SALVADOR\n"
        linea += "-----------------------------------------------------------------------------------\n"
        linea += "Chacón Sánchez, Salvador de Jesús: CS08004\n"
        linea += "Morales Álfaro, Daniel Enrique:    MA10016\n"
        linea += "Rivera Martínez, Kevin Edgardo:    RM11014\n"
        print(linea)
