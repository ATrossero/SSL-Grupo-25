import time
import tracemalloc


#Función de bubble_sort, que lo que hace es ordenar una lista de n elementos por orden numérico
def bubble_sort(lista):
    #n es el largo de la lista
    n = len(lista)
    for i in range(n):
        #lo hacemos tantas veces como lugares en la lista - 1
        for j in range(0, n - i - 1):
            #Si el número anterior es mayor al siguiente, intercambiamos el orden
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def main():
    # Harcodeamos la lista con números del 0 al 99 desordenado
    lista = [86, 45, 23, 97, 54, 19, 7, 61, 89, 72, 39, 2, 95, 68, 33, 17, 46, 90, 25, 77, 51, 82,
                    38, 60, 31, 26, 4, 99, 69, 88, 11, 56, 93, 5, 78, 21, 73, 8, 50, 16, 44, 29, 85, 12,
                    76, 96, 32, 70, 41, 64, 18, 63, 35, 91, 3, 15, 84, 37, 30, 98, 14, 58, 9, 49, 83, 22,
                    27, 65, 6, 75, 66, 47, 87, 80, 74, 53, 57, 10, 36, 59, 40, 48, 28, 81, 67, 94, 34, 24,
                    92, 13, 79, 43, 55, 71, 1,62,42,20,52]
    
    # Registramos el momento en donde inicia la ejecución de la función
    tracemalloc.start()
    #Registramos tiempo en el que va a iniciar la función de Fibonacci
    tiempo_inicio = time.time()
    #Se ejecuta la función
    bubble_sort(lista)
    #Registramos el momento en el que se termina de ejecutar la función
    tiempo_fin = time.time()
    #Calculamos la diferencia de tiempo para saber cuánto tomó
    tiempo_ejecucion = tiempo_fin - tiempo_inicio

    
    #Imprimimos los parámetros
    print("Lista ordenada:", lista)
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.15f} segundos")
    print(f"Uso de memoria:{tracemalloc.get_tracemalloc_memory()} bytes")
    #Una vez demostrado el uso de memoria podemos cerrar el registro.
    tracemalloc.stop()
if __name__ == "__main__":
    main()