import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv("Pokemon.csv", sep =",")
print(datos)
lista_ataque = list(datos["Attack"]) ; lista_num = list(datos["#"]) ; lista_tipo1 = list(datos["Type 1"])
lista_tipo2 = list(datos["Type 2"]) ; lista_nombres = list(datos["Name"]) ; lista_total = list(datos["Total"])
lista_HP = list(datos["HP"]) ; lista_defensa = list(datos["Defense"]) ; lista_SpA = list(datos["Sp. Atk"])
lista_SpD = list(datos["Sp. Def"]) ; lista_velocidad = list(datos["Speed"]) ; lista_generacion = list(datos["Generation"])
lista_legendario = list(datos["Legendary"])
class Analisis:
    def graficas():
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
        plt.subplot(2,3,1)
        plt.bar(lista_num, lista_ataque, color = "orange") ; plt.ylabel("Ataque") ; plt.xlabel("Nombre") ; plt.title("Ataque de los pokemon") ; plt.axhline(y=media_ataque, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.subplot(2,3,2)
        plt.bar(lista_num, lista_defensa, color = "blue") ; plt.ylabel("Defensa") ; plt.xlabel("Nombre") ; plt.title("Defensa de los pokemon") ; plt.axhline(y=media_def, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.subplot(2,3,3)
        plt.bar(lista_num, lista_velocidad, color = "red") ; plt.ylabel("Velocidad") ; plt.xlabel("Nombre") ; plt.title("Velocidad de los pokemon") ; plt.axhline(y=media_velocidad, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.subplot(2,3,4)
        plt.bar(lista_num, lista_SpA, color = "yellow") ; plt.ylabel("Ataque Especial") ; plt.xlabel("Nombre") ; plt.title("Ataque Especial de los pokemon") ; plt.axhline(y=media_SpA, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.subplot(2,3,5)
        plt.bar(lista_num, lista_SpD, color = "purple") ; plt.ylabel("Ataque") ; plt.xlabel("Nombre") ; plt.title("Defensa Especial de los pokemon") ;  plt.axhline(y=media_SpD, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.subplot(2,3,6)
        plt.bar(lista_num, lista_HP, color = "green") ; plt.ylabel("Puntos de Salud") ; plt.xlabel("Nombre") ; plt.title("Salud de los pokemon") ;  plt.axhline(y=media_hp, color="black", linestyle='solid', label = "media")
        plt.legend(loc='upper right')
        plt.show()
    def media(datos):
        mediatotal = datos["Total"].mean() ; mediaataque = datos["Attack"].mean() ; mediadefensa = datos["Defense"].mean() ; mediahp = datos["HP"].mean()
        mediaspatk = datos["Sp. Atk"].mean() ; mediaspdef = datos["Sp. Def"].mean() ; mediaspeed = datos["Speed"].mean()
        print("Media de la variable Total: ", mediatotal,"\nMedia de la variable Attack: ", mediaataque,"\nMedia de la variable Defense: ", mediadefensa,"\nMedia de la variable HP: ", mediahp,"\nMedia de la variable Sp. Atk: ", mediaspatk,"\nMedia de la variable Sp. Def: ", mediaspdef,"\nMedia de la variable Speed: ", mediaspeed)
    def varianza(datos):
        print("="*50)
        varianzatotal = datos["Total"].var() ; varianzaataque = datos["Attack"].var() ; varianzadefensa = datos["Defense"].var()
        varianzahp = datos["HP"].var() ; varianzaspatk = datos["Sp. Atk"].var() ; varianzaspdef = datos["Sp. Def"].var()
        varianzaspeed = datos["Speed"].var()
        print("Varianza de la variable Total: ", varianzatotal,"\nVarianza de la variable Attack: ", varianzaataque,"\nVarianza de la variable Defense: ", varianzadefensa,"\nVarianza de la variable HP: ", varianzahp,"\nVarianza de la variable Sp. Atk: ", varianzaspatk,"\nVarianza de la variable Sp. Def: ", varianzaspdef,"\nVarianza de la variable Speed: ", varianzaspeed)
    def desviacion(datos):
        print("="*50)
        desviaciontotal = datos["Total"].std() ; desviacionataque = datos["Attack"].std() ; desviaciondefensa = datos["Defense"].std()
        desviacionhp = datos["HP"].std() ; desviacionspatk = datos["Sp. Atk"].std() ; desviacionspdef = datos["Sp. Def"].std() ; desviacionspeed = datos["Speed"].std()
        print("Desviacion estandar de la variable Total: ", desviaciontotal,"\nDesviacion estandar de la variable Attack: ", desviacionataque,"\nDesviacion estandar de la variable Defense: ", desviaciondefensa,"\nDesviacion estandar de la variable HP: ", desviacionhp,"\nDesviacion estandar de la variable Sp. Atk: ", desviacionspatk,"\nDesviacion estandar de la variable Sp. Def: ", desviacionspdef,"\nDesviacion estandar de la variable Speed: ", desviacionspeed)
    def sacar_maximos():
        max_atq = max(lista_ataque) ; indice_ataque = lista_ataque.index(max_atq) ; ataque_max = datos.iloc[indice_ataque]
        print(f"El pokemon con más ataque es: \n {ataque_max}")
        max_HP = max(lista_HP) ; indice_HP = lista_HP.index(max_HP) ; HP_max = datos.iloc[indice_HP]
        print(f"El pokemon con más Puntos de Salud es: \n {HP_max}")
        max_velocidad = max(lista_velocidad) ; indice_velocidad = lista_velocidad.index(max_velocidad) ; Velocidad_max = datos.iloc[indice_velocidad]
        print(f"El pokemon con más velocidad es: \n {Velocidad_max}")
        max_SpA = max(lista_SpA) ; indice_Spa = lista_SpA.index(max_SpA) ; spa_max = datos.iloc[indice_Spa]
        print(f"El pokemon con más ataque especial es:  \n {spa_max}")
        max_SpD = max(lista_SpD) ; indice_Spd = lista_SpD.index(max_SpD) ; spd_max = datos.iloc[indice_Spd]
        print(f"El pokemon con más defensa especial es: \n {spd_max}")
        max_def = max(lista_defensa) ; indice_def = lista_defensa.index(max_def) ; def_max = datos.iloc[indice_def]
        print(f"El pokemon con más defensa es: \n {def_max}")
        print("\n \n Los pokemon que usaré serán: MewtwoMega Mewtwo X, Blissey, DeoxysSpeed Forme, MewtwoMega Mewtwo Y, Shuckle, SteelixMega Steelix")

Analisis.graficas()
Analisis.media(datos)
Analisis.varianza(datos)
Analisis.desviacion(datos)
Analisis.sacar_maximos()