"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos geneticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Profesor: Dr. Asdrubal Lopez Chau

Descripción:  Script de pruebas

Created on May  22 13:33:22 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8


@author: angel
"""
import numpy as np
from AlgoritmoEvolutivo import AlgoritmoEvolutivo
from GenReal import GenReal as Real
from CromosomaReal import CromosomaReal as CReal
import matplotlib.pyplot as mp 
import os
import fn



vol = float(input("Ingresa el punto inicial de busqueda: "))
print()
it=int(input('De el numero de iteraciones: '))
print()

k = np.power(vol, 1/3)
# Minis y Maxis
minis = [k/6 , k/8, 12*k]
maxis = [k/3, k/4, 6*k]
nbits = [16,32,64]

#cromosoma creado y agregado a los minis y maximos  
CromoN = []
#Por cada individuo generedo se agregaran a los nuevos minimos y maximos 
for i in range(100):
    individuos = CReal(minis, maxis,nbits)
    individuos.init()
    #Cromomosa para los 10 individuos
    CromoN.append(individuos)
    
#Cruza 2 individuos e imprime a los dos hijos
papa = CromoN[0]
mama = CromoN[-1]

##Cruza entre el padre y la madre para la generecion de los hijos
Hijos = papa.cruzar(mama)

class CromosomaN:
    #Minimos y maximos para el trabajo y proceso de los genes
    def __init__(self, minis, maxis,nbits):
        if len (minis) != len (maxis):
            return
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.genes = []
        for min, max in zip (minis, maxis,nbits):
            gen = Real (min, max)
            self.genes.append(gen)
    #Cada gen generado ira tomando su lugar entre 0 y 1
    def init(self):
        for gen in self.genes:
            gen.initGen()
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

#Inicializacion  guiada 

ca2 = AlgoritmoEvolutivo(100, vol, minis, maxis, nbits)
ca2.inicializa()
print("Primer generacion")
print()
#print(papa.__str__())
#print(papa.getValues())
ca2.showPob(True)

for i in range(100):

    ca2.evolucion()

print()
print("Segunda generacion")
print()

ca2.showPob(True)
print()
#print(mama.__str__())
#print(mama.getValues())
#Pruebas ejecutadas dentro del algoritmo evolutivo 
ca2.Ca()

os.system("cls")

#vol=float(input('De el punto inicial de busqueda: '))
k=int(1)
tol=float(pow(10,-5))
err=float(5.0)
fc1=float(125.0)
print('\n Raices encontradas')
print('k \t x0 \t fc \t err')

while(k < it and err > tol):
    fc=fn.f0(vol)
    fpc=fn.fp(vol)
    if fpc ==0:
       print('La derivada es igual a cero')
       break
    else:
      x1=vol-(fc/fpc)
      err=np.linalg.norm(x1-vol)
      print(k ,'\t',vol,'\t',fc,'\t',err)
      vol=x1
      k+=1
if(abs(fc) < tol or err < tol):
    print('\nAproximacion a la raiz es',vol)
else:
    print('\nEsta divirgiendo u oscilando')
    
x=np.linspace(vol-5,vol+5,100)
y1=(fn.f0)(x)
figure, ax = mp.subplots()
ax.plot(x,y1)
ax.grid()
mp.show()
