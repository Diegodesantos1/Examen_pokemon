import pandas as pnd
import JMPEstadisticas as jmp

def analisis_estadisticas():
    eleccion = int(input(("Qué estadística quieres ver? Elige de que stat quieres la estadística(el total(1), hp(2), attack(3), defense(4), sp.attack(5), sp.defense(6), speed(7)\n")))
    if eleccion == 4:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Defense"])
        observaciones = pnd.DataFrame({'Defensa': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Defensa'])
        stats.analisisCaracteristica()
    if eleccion == 3:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Attack"])
        observaciones = pnd.DataFrame({'Ataque': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Ataque'])
        stats.analisisCaracteristica()
    if eleccion == 7:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Speed"])
        observaciones = pnd.DataFrame({'Velocidad': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Velocidad'])
        stats.analisisCaracteristica()
    if eleccion == 2:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["HP"])
        observaciones = pnd.DataFrame({'Puntos de Vida': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Puntos de Vida'])
        stats.analisisCaracteristica()
    if eleccion == 5:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Sp. Atk"])
        observaciones = pnd.DataFrame({'Ataque Especial': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Ataque Especial'])
        stats.analisisCaracteristica()
    if eleccion == 6:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Sp. Def"])
        observaciones = pnd.DataFrame({'Defensa Especial': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Defensa Especial'])
        stats.analisisCaracteristica()
    if eleccion == 1:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Total"])
        observaciones = pnd.DataFrame({'Total': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Total'])
        stats.analisisCaracteristica()
analisis_estadisticas()