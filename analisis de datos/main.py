import pandas as pnd
import JMPEstadisticas as jmp

if __name__ == '__main__':
        datos = pnd.read_csv("Pokemon.csv", header=0 , sep =",")
        lista_notas = list(datos["Type"])
        observaciones = pnd.DataFrame({'Type': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['Type'])
        stats.analisisCaracteristica()
