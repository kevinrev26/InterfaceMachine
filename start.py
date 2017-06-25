#!/usr/bin/env python
# Título: 
# Autor: Kevin Rivera
# Descripción: Punto de entrada para la programación de la simulación

# Importando librerias necesarias
from utilidades import Simulacion


if __name__ == '__main__':

    try:
        iteraciones = int(input("Ingrese el numero de iteraciones: "))
        modelo = Simulacion.Simulacion(iteraciones)
        modelo.simular()
    except ValueError:
        print("No ha ingresado un numero, ejecute de nuevo")