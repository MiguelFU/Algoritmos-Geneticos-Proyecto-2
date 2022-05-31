"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Profesor: Dr. Asdrúbal López Chau

Descripción:  Mecanismo de selección

Created on Mon May  25 09:38:30 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8


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
