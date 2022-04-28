import pandas as pnd
import JMPEstadisticas as jmp
import modules_old


if __name__ == '__main__':
    eleccion = int(input(("¿Qué quieres ejecutar? \n 1: Juego de Pokémon \n 2: Análisis de Datos\n")))
    if eleccion == 1:
        import modules_old
    elif eleccion ==2:
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Type"])
        observaciones = pnd.DataFrame({'Type': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Type'])
        stats.analisisCaracteristica()
