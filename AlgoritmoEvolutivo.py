"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina
        
Profesor: Dr. Asdrúbal López Chau

Descripción:  Algoritmo genético Proyecto 2

Created on Mon May  20 12:48:33 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8

@author: angel
"""
import numpy as np
import random
from Poblacion import Poblacion
from FitnessFunction import FitnessFunction
from Seleccion import Seleccion
from collections import OrderedDict
from GenReal import GenReal as Real


class AlgoritmoEvolutivo: #Declaramos los parametros del algoritmo evolutivo 
                          #Tamaño de la poblacion
                          #Numero de generaciones
                          #Porcentaje de mutacion
                          #Grado de similitud en la poblacion

    def __init__(self, size, target, minis, maxis, nbits):
        self.target = target
        self.size = size
        self.minis = minis
        self.maxis = maxis
        self.nbits = nbits
        self.pob = None

    def showPob(self, showAptitude=False):#Aptitudes de la poblacion para la seleccion de la misma y el trabajo que se dara para la mutacion

        if showAptitude:
            aptitudes = [self.ff.evaluate(ind)
                     for ind in self.pob.poblacion]

        for i in range(self.size):
            if showAptitude:
                print(self.pob.poblacion[i].cromosoma.getValues() ,
                      " -> " + str(aptitudes[i]))
            else:
                print(self.pob.poblacion[i])
    
    #Minimos y maximos para el trabajo y proceso de los genes
    def __initG__(self, minis, maxis, nbits):
        if len (minis) != len (maxis):
            return
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.nbits = nbits.copy()
        self.genes = []
        for min, max, nbits in zip (minis, maxis, nbits):
            gen = Real (min, max, nbits)
            self.genes.append(gen)
    #Cada gen generado ira tomando su lugar entre 0 y 1
    def init(self):
        for gen in self.genes:
            gen.init()
    #gen creado y agregado a los genes nuevos 
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad
    #Evalua y verfica el gen generado en genes
    def getValues(self):
        values = []
        for gen in self.genes:
            values.append(gen.getValue())
        return values
    #Cruza del padre y la madre para los hijos entre el gen y los genes verificados
    def cruzar(self, madre):
        genesHijos1 = []
        genesHijos2 = []
        for papa, mama in  zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genesHijos1.append(g[0])
            genesHijos2.append(g[1])
        h1 = Real(self.minis, self.maxis, self.nbits)
        h2 = Real(self.minis, self.maxis, self.nbits)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]


    def evolucion(self):
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población
        ####### Implementación #############
        if self.pob is None:
            print("Inicialice la población")
            return
        #1) Evaluar individuos
        poblacion = self.pob.poblacion        
        aptitudes = [self.ff.evaluate(ind) 
                     for ind in poblacion]
        # # 2) Seleccionar padres para cruza
        k = int(self.size/2)
        if k%2 == 1:
            k += 1
        idx = self.seleccion.selecciona(aptitudes,k)
        #3) Generar hijos (cruza)
        descendencia = []
        for i in list(range(0,k-1,2)):
            ip = idx[i]
            im = idx[i+1]
            papa = poblacion[ip]
            mama = poblacion[im]
            hijos = papa.cruza(mama)
            descendencia.append(hijos[0])
            descendencia.append(hijos[1])
        
        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.1))
        
        for i in range(totalMutar):
            idx = random.choice(range(len(descendencia)))
            descendencia[idx].mutar()
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente 
        #     población
        
        # Junto padres e hijos
        for hijo in descendencia:
            poblacion.append(hijo)
        # calculo aptitudes de todos
        aptitudes = [self.ff.evaluate(ind) 
                     for ind in poblacion]
        # ELITISMO!!!!!
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        # Selecciono indices de
        # individuos para la siguiente generacion
        idx = self.seleccion.selecciona(aptitudes,
                                  self.size)
        # Creo la lista de individuos de la siguiente
        # generación

        for i in idx:
            siguientePob.append(poblacion[i])
        # Guardo para la siguiente evolución
        self.pob.poblacion = siguientePob
        
    def Ca(self):
        poblacion2 = self.pob
        aptitudes = [self.ff.evaluate(ind)
                 for ind in self.pob.poblacion]
        valores = []

        # generación

        aptitudes = list(OrderedDict.fromkeys(aptitudes))
        poblacion2.poblacion = list(OrderedDict.fromkeys(poblacion2.poblacion))
        
        #Guardo para la siguiente evolución


        for i in range(5):
            max_value = max(aptitudes)
            indice = aptitudes.index(max_value)
            valores.append(poblacion2.poblacion[indice].cromosoma.getValues())
            poblacion2.poblacion.pop(indice)
            aptitudes.pop(indice)
        
         # Creo la lista de individuos de la siguiente

        print()
            
    def inicializa(self):
        pob = Poblacion(self.size, self.minis, self.maxis, self.nbits)
        pob.inicializa()
        self.pob = pob
        self.seleccion = Seleccion()
        self.ff = FitnessFunction(self.target)
