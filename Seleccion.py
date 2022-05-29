"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Descripción:  Mecanismo de selección

Created on Mon May  25 09:38:30 2022

@author: angel
"""
import numpy as np
import random
class Seleccion: #En esta clase seleccionamos las aptitudes y las probabilidades de la poblacion para la generacion 
                 #De nuevos individuos 



    def selecciona(self, aptitudes, k=2):
        # Darle chance a los feos
        aptitudes = np.array(aptitudes) + .01
        '''
        denom = np.sum(np.exp(aptitudes))
        probabilidades = []
        for aptitud in aptitudes:
            probabilidades.append(np.exp(aptitud)/denom)
        '''
        #Probabilidades dentro de las aptitudes inicializados aleatoriamente.
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes))
                  for aptitud
                  in aptitudes]
        indices = list(range(len(aptitudes)))
        return random.choices(indices, probabilidades, k=k)
