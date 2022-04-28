import pandas as pnd
import JMPEstadisticas as jmp


if __name__ == '__main__':
    eleccion = int(input(("¿Qué quieres ejecutar? \n 1: Juego de Pokémon \n 2: Análisis de Datos\n")))
    if eleccion == 1:
        pass
    elif eleccion ==2:
        datos = pnd.read_csv("imdb_sup.csv", header=0 , sep =",")
        lista_notas = list(datos["Rating"])
        observaciones = pnd.DataFrame({'NOTAS': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['NOTAS'])
        stats.analisisCaracteristica()
