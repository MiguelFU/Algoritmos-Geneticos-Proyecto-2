"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Geneticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Profesor: Dr. Asdrúbal López Chau

Descripción:  Clase Individuo para poiinomios

Created on Mon May 26 10:26:10 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8


@author: angel
"""

from CromosomaReal import CromosomaReal as Real
class Individuo:
    
    """
    Generamos a nuestros individuos, utilzando la generacion de la contraseña
    a) como base tomamos en cuenta el abcedario 
    """

    def __init__(self, minis, maxis, nbits):
       #self.alfabeto = "abcdefghijklmnopqrtsuvwxyz"
        #self.cromosoma = ""
        self.minis = minis
        self.maxis = maxis
        self.nbits = nbits
        self.cromosoma = Real(self.minis, self.maxis, self.nbits)
        #Cromosoma para la descomposicion

    def init(self):
        #self.cromosoma = ''.join(random.choices(self.alfabeto, k=sizeInd))
        #self.sizeInd = sizeInd 
        self.cromosoma.init()
        #Genera un cromosoma aleatorio, con los minis y maxis que nos dieron , este caso el tamaño del cromosoma es el numero de bits


    #Operador de mutacion y de cruza
    #Cruzamos al padre y a la madre
    #Generemos a los nuevos hijos
    #Grado de similitud en la poblacion
    #Individuos generados en la poblacion 
    def cruza(self, mother):# Elementos del algoritmo evolutivo 
        papa = Real(self.minis, self.maxis, self.nbits)
        papa.init()
        #son1 = padre[0:mitad] + madre[mitad:]
        #son2 = madre[0:mitad] + padre[mitad:]
        mama = Real(self.minis, self.maxis, self.nbits)
        mama.init()
        hijos = papa.cruzar(mama)
        ind1 = Individuo(self.minis, self.maxis, self.nbits)
        ind1.cromosoma = hijos[0]
        ind2 = Individuo(self.minis, self.maxis, self.nbits)
        ind2.cromosoma = hijos[1]
        return [ind1, ind2]
    #Cromosoma 
    def __str__(self):
        return self.cromosoma.__str__()

    #Mutamos algunos de los nuevos individuos, con sus cromosomas.
    def mutar(self):
        #idx = np.random.randint(self.sizeInd)
        #cambiar = ''.join(random.choices(self.alfabeto, k=1))
        self.cromosoma.mutar()
