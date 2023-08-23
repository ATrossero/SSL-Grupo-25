import time
import tracemalloc


#Algoritmo que realiza la función de fibonacci de un número n.
def fibonacci(n):
    #Casos base
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        #Caso recursivo
        secuencia_fibonacci = [0, 1]
        for i in range(2, n):
            #se agrega a la lista el cálculo del número siguiente de la secuencia
            secuencia_fibonacci.append(secuencia_fibonacci[i - 1] + secuencia_fibonacci[i - 2])
        return secuencia_fibonacci

def main():
    #Número n de fibonacci a calcular
    n = 150
    #Iniciamos el registro de la memoria consumida del programa
    tracemalloc.start()
    #Registramos tiempo en el que va a iniciar la función de Fibonacci
    tiempo_inicio = time.time()
    #Se ejecuta la función
    secuencia_fibonacci = fibonacci(n)
    #Registramos el momento en el que se termina de ejecutar la función
    tiempo_fin = time.time()
    #Calculamos la diferencia de tiempo para saber cuánto tomó
    tiempo_ejecucion = tiempo_fin - tiempo_inicio

    
    #Imprimimos los parámetros
    print("Secuencia de Fibonacci:", secuencia_fibonacci)
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.15f} segundos")
    print(f"Uso de memoria:{tracemalloc.get_tracemalloc_memory()} bytes")
    #Una vez demostrado el uso de memoria podemos cerrar el registro.
    tracemalloc.stop()

if __name__ == "__main__":
    main()