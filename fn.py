"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Tema:Proyecto 2 Algoritmos Geneticos 

Author: Miguel Angel Flores Urbina
        Luis Angel Dias Navas
        Leonardo Villanueva Medina

Profesor: Dr. Asdrúbal López Chau

Descripción:  Funciones de  polinomios

Created on Mon May  26 11:58:44 2022

Enlace del video: https://www.youtube.com/watch?v=C9F6cKH1KGQ

Enlace de GitGub: https://github.com/MiguelFU/Algoritmos-Geneticos-Proyecto-2?fbclid=IwAR0aGxPM3mDM3gG9TPONVleBuLGNvjqgHC7O-kxEWMUQ0bRCsZLIOxbN6g8


@author: angel
"""

f0=lambda x:pow(x,2)+3*pow(x,1)-5
fp=lambda x:2*pow(x,1)+3

#f0=lambda x:pow(x,10)-1
#fp=lambda x: 10*pow(x,9)
#f0=lambda x:exp(-x)-x
#fp=lambda x:-exp(-x)-1
#f0=lambda x:pow (x,6)-8
#fp=lambda x:6*pow(x,5)
#Ejercicios 05/10/2020
#f0=lambda x:pow (x,5)-3
#fp=lambda x:5*pow(x,4)

#Ejercicios 05/10/2020
#f0=lambda x:9*pow(x,3)-5*pow(x,2)+18*x-5
#fp=lambda x:27*pow(x,2)-10*x+18

#f0 =lambda x:-0.58*pow(x,2)+2.5*x+4.5
#f0 = lambda x : pow(x,3)-2*sin(x)
#f0 = lambda x : pow(x,3) - 3*x + 1
#f0 = lambda x:3*pow(x,3)-7*pow(x,2)+6*x+5

        #Ejercicios 
#Ejercicio 5.1, pag 110
#f0 = lambda x: (-0.5)*pow(x,2) + 2.5*pow(x,1) + 4.5


#f0 = lambda x:-25 + 82*x - 9*pow(x,2) + 44*pow(x,3) - 8*pow(x,4) + 0.7*pow(x,5)


#f0 = lambda x: -12 - 21*x + 18*pow(x,2) - 2.75*pow(x,3)


#f0 = lambda x:  (0.8 - 0.3*x)/x
