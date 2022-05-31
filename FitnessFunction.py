"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Geneticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Profesor: Dr. Asdrúbal López Chau

Descripción:  Clase fitnessfunction
evalua individuos para el problema de polinomios

Created on Mon May  22 11:13:53 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8


@author: angel
"""
import numpy as np
class FitnessFunction:

    def __init__(self, target):
        #Es la evaluacion 
        self.target = target
        self.lamda = 1
        self.beta = 1

    def evaluate(self, ind):
        '''
        Evalua la aptitud de un individuo
        Parameters
        ----------
        ind : Individuo
            DESCRIPTION. Representa una
            contraseña

        Returns
        -------
        int
            DESCRIPTION. Aptitud del
            individuo es la cantidad de
            letras en la posicion correcta
            '''
        #print("ESTE ES TARGET ", self.target)
        ladC = ind.cromosoma.getValues()
        vol = 1
        for lado in ladC:
            vol = vol * lado
        #print(self.target - vol)
        x = np.abs(self.target - vol)
        return self.beta*np.exp(-self.lamda * x)
