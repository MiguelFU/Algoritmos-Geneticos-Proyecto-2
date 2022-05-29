"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Geneticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina
Descripción:  Población de individuos


Created on Mon May  25 11:31:12 2022

@author: angel
"""
from Individuo import Individuo
#Seleccionamos a la poblacion 
#Conservamos la mejor solucion hasta el momento 
class Poblacion:

    def __init__(self, size, minis, maxis, nbits):
        #self.target = target
        self.size = size
        self.nbits = nbits
        self.maxis = maxis
        self.minis = minis
        
    #Con nuestros mecanismos de seleccion se considera la aptitud de los individuos
    #Grado de similitud en la poblacion
    #Tamaño de la poblacion

    def inicializa(self):
        poblacion = []
        for i in range(self.size):
            #ind = Individuo()
            #ind.sizeInd = len(self.target)
            ind = Individuo(self.minis, self.maxis, self.nbits)
            ind.init()
            poblacion.append(ind)
        self.poblacion = poblacion
