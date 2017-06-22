#!/usr/bin/env python
# Título: 
# Autor: Kevin Rivera
# Descripción:

import math

class Arreglo():


    def __init__(self, *datos):
        self.maquinas = list(datos)


    def encontrarMinimo(self):
        #print("iterando: ", type(self.maquinas))
        indice = 0
        aux = 9000
        for e in self.maquinas:
            if not math.isnan(e):
                if e <= aux:
                    index = index +1

        return index

    def getValue(self,index):
        return self.maquinas[index]

    def setValue(self,index, value):
        self.maquinas[index] = value

    def devolverIndiceElemento(self,elemento):
        return self.maquinas.index(elemento)

    def longitud(self):
        return len(self.maquinas)

    def includes(self, elemento):
        return elemento in self.maquinas

    def indexOf(self, value):
        return self.maquinas.index(value)

    def imprimir(self):
        print(self.maquinas)
