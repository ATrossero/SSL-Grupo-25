import time
import tracemalloc


#Función de bubble_sort, que lo que hace es ordenar una lista de n elementos por orden numérico
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Harcodeamos la lista con números del 0 al 99 desordenado
    unsorted_list = [86, 45, 23, 97, 54, 19, 7, 61, 89, 72, 39, 2, 95, 68, 33, 17, 46, 90, 25, 77, 51, 82,
                    38, 60, 31, 26, 4, 99, 69, 88, 11, 56, 93, 5, 78, 21, 73, 8, 50, 16, 44, 29, 85, 12,
                    76, 96, 32, 70, 41, 64, 18, 63, 35, 91, 3, 15, 84, 37, 30, 98, 14, 58, 9, 49, 83, 22,
                    27, 65, 6, 75, 66, 47, 87, 80, 74, 53, 57, 10, 36, 59, 40, 48, 28, 81, 67, 94, 34, 24,
                    92, 13, 79, 43, 55, 71, 1,62,42,20,52]
    
    # Registramos el momento en donde inicia la ejecución de la función
    tracemalloc.start()

    # empezamos a cronometrar el tiempo de ejecución
    start_time = time.time()

    # ejecutamos la función a analizar con la lista 
    bubble_sort(unsorted_list)

    # Registramos el tiempo en el que finalizó la función
    end_time = time.time()
    #Calculamos la diferencia de tiempo para saber cuánto tomó
    execution_time = end_time - start_time

    # Imprimimos los parámetros

    print("Lista ordenada:", unsorted_list)
    print(f"Tiempo de ejecución: {execution_time:.12f} segundos")
    print("Uso de memoria adicional durante la ejecución:", tracemalloc.get_tracemalloc_memory(), "bytes")
    #Frenamos el uso de memoria una vez ya escrito en el printf.
    tracemalloc.stop()
if __name__ == "__main__":
    main()