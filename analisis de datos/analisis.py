import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv("Pokemon.csv", sep =",")
print(datos)
def graficas():
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
def media(datos):
    mediatotal = datos["Total"].mean() ; mediaataque = datos["Attack"].mean() ; mediadefensa = datos["Defense"].mean() ; mediahp = datos["HP"].mean()
    mediaspatk = datos["Sp. Atk"].mean() ; mediaspdef = datos["Sp. Def"].mean() ; mediaspeed = datos["Speed"].mean()
    print("Media de la variable Total: ", mediatotal,"\nMedia de la variable Attack: ", mediaataque,"\nMedia de la variable Defense: ", mediadefensa,"\nMedia de la variable HP: ", mediahp,"\nMedia de la variable Sp. Atk: ", mediaspatk,"\nMedia de la variable Sp. Def: ", mediaspdef,"\nMedia de la variable Speed: ", mediaspeed)
    media(datos)

def varianza(datos):
    print("="*50)
    varianzatotal = datos["Total"].var() ; varianzaataque = datos["Attack"].var() ; varianzadefensa = datos["Defense"].var()
    varianzahp = datos["HP"].var() ; varianzaspatk = datos["Sp. Atk"].var() ; varianzaspdef = datos["Sp. Def"].var()
    varianzaspeed = datos["Speed"].var()
    print("Varianza de la variable Total: ", varianzatotal,"\nVarianza de la variable Attack: ", varianzaataque,"\nVarianza de la variable Defense: ", varianzadefensa,"\nVarianza de la variable HP: ", varianzahp,"\nVarianza de la variable Sp. Atk: ", varianzaspatk,"\nVarianza de la variable Sp. Def: ", varianzaspdef,"\nVarianza de la variable Speed: ", varianzaspeed)
varianza(datos)

def desviacion(datos):
    print("="*50)
    desviaciontotal = datos["Total"].std() ; desviacionataque = datos["Attack"].std() ; desviaciondefensa = datos["Defense"].std()
    desviacionhp = datos["HP"].std() ; desviacionspatk = datos["Sp. Atk"].std() ; desviacionspdef = datos["Sp. Def"].std() ; desviacionspeed = datos["Speed"].std()
    print("Desviacion estandar de la variable Total: ", desviaciontotal,"\nDesviacion estandar de la variable Attack: ", desviacionataque,"\nDesviacion estandar de la variable Defense: ", desviaciondefensa,"\nDesviacion estandar de la variable HP: ", desviacionhp,"\nDesviacion estandar de la variable Sp. Atk: ", desviacionspatk,"\nDesviacion estandar de la variable Sp. Def: ", desviacionspdef,"\nDesviacion estandar de la variable Speed: ", desviacionspeed)




def media(datos):
    mediatotal = datos["Total"].mean() ; mediaataque = datos["Attack"].mean() ; mediadefensa = datos["Defense"].mean() ; mediahp = datos["HP"].mean()
    mediaspatk = datos["Sp. Atk"].mean() ; mediaspdef = datos["Sp. Def"].mean() ; mediaspeed = datos["Speed"].mean()
    print("Media de la variable Total: ", mediatotal,"\nMedia de la variable Attack: ", mediaataque,"\nMedia de la variable Defense: ", mediadefensa,"\nMedia de la variable HP: ", mediahp,"\nMedia de la variable Sp. Atk: ", mediaspatk,"\nMedia de la variable Sp. Def: ", mediaspdef,"\nMedia de la variable Speed: ", mediaspeed)
media(datos)

def varianza(datos):
    print("="*50)
    varianzatotal = datos["Total"].var() ; varianzaataque = datos["Attack"].var() ; varianzadefensa = datos["Defense"].var()
    varianzahp = datos["HP"].var() ; varianzaspatk = datos["Sp. Atk"].var() ; varianzaspdef = datos["Sp. Def"].var()
    varianzaspeed = datos["Speed"].var()
    print("Varianza de la variable Total: ", varianzatotal,"\nVarianza de la variable Attack: ", varianzaataque,"\nVarianza de la variable Defense: ", varianzadefensa,"\nVarianza de la variable HP: ", varianzahp,"\nVarianza de la variable Sp. Atk: ", varianzaspatk,"\nVarianza de la variable Sp. Def: ", varianzaspdef,"\nVarianza de la variable Speed: ", varianzaspeed)
varianza(datos)

def desviacion(datos):
    print("="*50)
    desviaciontotal = datos["Total"].std() ; desviacionataque = datos["Attack"].std() ; desviaciondefensa = datos["Defense"].std()
    desviacionhp = datos["HP"].std() ; desviacionspatk = datos["Sp. Atk"].std() ; desviacionspdef = datos["Sp. Def"].std() ; desviacionspeed = datos["Speed"].std()
    print("Desviacion estandar de la variable Total: ", desviaciontotal,"\nDesviacion estandar de la variable Attack: ", desviacionataque,"\nDesviacion estandar de la variable Defense: ", desviaciondefensa,"\nDesviacion estandar de la variable HP: ", desviacionhp,"\nDesviacion estandar de la variable Sp. Atk: ", desviacionspatk,"\nDesviacion estandar de la variable Sp. Def: ", desviacionspdef,"\nDesviacion estandar de la variable Speed: ", desviacionspeed)
desviacion(datos)