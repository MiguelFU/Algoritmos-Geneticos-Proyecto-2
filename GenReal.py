"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: ALGORITMOS GENETICOS
Tema: Proyecto 2 Algoritmos Geneticos 
Alumnos: Miguel Angel Flores Urbina
         Luis Angel Diaz Navas
         Villa Nueva Medina leonardo
Profesor: Dr. Asdrúbal López Chau
Descripción: Gen real  para AG 
Created on Mon May 25 18:27:06 2022

@author: angel
"""
import numpy as np
import random

class GenReal:
    def __init__(self,min,max,nbits):
        #Calcula el numero de bits necesarios
        self.min=min
        self.max=max
        self.nbits=nbits
        self.delta=np.abs(min-max)/2**nbits

    
    def init(self):
        #Inicializa el gen aleatoriamente con ceros y unos
        self.gen = random.choices([0, 1], k=self.nbits)
    
    def cruzar(self,mama):
        #aplica la cruza de este gen con el gen de la madre
        padre = self.gen.copy()
        madre = mama.gen.copy()
        cp1 = int(np.ceil((self.nbits - 1)/3.))
        cp2 = 2 * cp1
        son1 = padre[0:cp1]
        son1.extend(madre[cp1:cp2])
        son1.extend(padre[cp2:])
        
        son2 = madre[0:cp1]
        son2.extend(padre[cp1:cp2])
        son2.extend(madre[cp2:])
        
        s1 = GenReal(self.min, self.max,self.nbits)
        s2 = GenReal(self.min, self.max,self.nbits)
        s1.gen = son1
        s2.gen = son2
        return [s1, s2]
    
    def mutar(self):
        self.init()
    
    def __str__(self):
        #Regresa el gen como cadena de ceros y unos
        return str(self.gen)
    
    def getValue(self):
        #Regresa el valor entero que representa el gen
        particion = int(''.join([str(i) for i in self.gen]), 2)
        return self.min + self.delta*particion