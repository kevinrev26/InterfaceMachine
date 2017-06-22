#!/usr/bin/env python
# Título: 
# Autor: Kevin Rivera
# Descripción:
from .Arreglo import Arreglo

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

    def llegada(self):
        print("Ha ocurrido una llegada")
        self.masterClock = self.vector.getValue(self.indice)

        if self.n == 0:
            self.mecanico = 1
            self.vector.setValue(len(self.vector)-1,self.masterClock +5)
            self.n=1
            self.vector.setValue(self.indice,'REPARACION')
        else:
            self.n += 1
            #TODO Agregar a la cola
            self.vector.setValue(self.indice,'EN ESPERA')


    def salida(self):
        print("Ha ocurrido una salida")


    def simular(self):
        print("Simulacion comenzada")
