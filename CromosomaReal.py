"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: ALGORITMOS GENETICOS
Tema: Proyecto 2 Algortimos Geneticos
Alumnos: Miguel Angel Flores Urbina
         Luis Angel Diaz Navas
         Villa Nueva Medina leonardo
Profesor: Dr. Asdrúbal López Chau
Descripción: Cromosoma real para AG 
Created on Mon May 25 18:27:21 2022

@author: angel
"""

from GenReal import GenReal as Real

class CromosomaReal:
    #Minimos y maximos para el trabajo y proceso de los genes
    def __init__(self, minis, maxis, nbits):
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
        h1 = CromosomaReal(self.minis, self.maxis, self.nbits)
        h2 = CromosomaReal(self.minis, self.maxis, self.nbits)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
            
    def mutar (self):
        #Cada gen generado en genes ira mutando en el gen
        for gen in self.genes:
            gen.mutar()