import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
import math
class Grafica:
    global datos
    datos = pd.read_csv("Pokemon.csv", sep =";")
    def grafica_inicial():
        lista_ataque = list(datos["Attack"]) ; lista_num = list(datos["#"]) ; lista_tipo1 = list(datos["Type 1"])
        lista_tipo2 = list(datos["Type 2"]) ; lista_nombres = list(datos["Name"]) ; lista_total = list(datos["Total"])
        lista_HP = list(datos["HP"]) ; lista_defensa = list(datos["Defence"]) ; lista_SpA = list(datos["Sp. Atk"])
        lista_SpD = list(datos["Sp. Def"]) ; lista_velocidad = list(datos["Speed"]) ; lista_generacion = list(datos["Generation"])
        lista_legendario = list(datos["Legendary"])
        a = 0 ; b = 0 ; c = 0 ; d = 0 ; e = 0 ; f = 0 ; g = 0
        for i in lista_ataque:
            a += i
        media_ataque = a/len(lista_ataque)
        for i in lista_defensa:
            b += i
        media_def = b/len(lista_defensa)
        for i in lista_HP:
            c += i
        media_hp = c/len(lista_HP)
        for i in lista_velocidad:
            d += i
        media_velocidad = d/len(lista_velocidad)
        for i in lista_SpA:
            e += i
        media_SpA= d/len(lista_SpA)
        for i in lista_SpD:
            f += i
        media_SpD= d/len(lista_SpD)
        plt.subplot(3,3,1)
        plt.bar(lista_nombres, lista_ataque, color = "green") ; plt.ylabel("Ataque") ; plt.xlabel("Nombre") ; plt.title("Ataque de los pokemon") ; plt.axhline(y=media_ataque, color="black", linestyle='solid')
        plt.subplot(3,3,2)
        plt.bar(lista_nombres, lista_defensa, color = "green") ; plt.ylabel("Defensa") ; plt.xlabel("Nombre") ; plt.title("Defensa de los pokemon") ; plt.axhline(y=media_def, color="black", linestyle='solid')
        plt.subplot(3,3,3)
        plt.bar(lista_nombres, lista_velocidad, color = "green") ; plt.ylabel("Velocidad") ; plt.xlabel("Nombre") ; plt.title("Velocidad de los pokemon") ; plt.axhline(y=media_velocidad, color="black", linestyle='solid')
        plt.subplot(3,3,4)
        plt.bar(lista_nombres, lista_SpA, color = "green") ; plt.ylabel("Ataque Especial") ; plt.xlabel("Nombre") ; plt.title("Ataque Especial de los pokemon") ; plt.axhline(y=media_SpA, color="black", linestyle='solid')
        plt.subplot(3,3,5)
        plt.bar(lista_nombres, lista_SpD, color = "green") ; plt.ylabel("Ataque") ; plt.xlabel("Nombre") ; plt.title("defensa Especial de los pokemon") ;  plt.axhline(y=media_SpD, color="black", linestyle='solid')
        plt.subplot(3,3,6)
        plt.bar(lista_nombres, lista_HP, color = "green") ; plt.ylabel("Puntos de Salud") ; plt.xlabel("Nombre") ; plt.title("Salud de los pokemon") ;  plt.axhline(y=media_hp, color="black", linestyle='solid')
        plt.show()
Grafica.grafica_inicial()