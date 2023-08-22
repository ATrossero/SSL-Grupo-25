import time
import tracemalloc


#Algoritmo que realiza la función de fibonacci de un número n.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence

def main():
    #Número n de fibonacci a calcular
    n = 150
    #Iniciamos el registro de la memoria consumida del programa
    tracemalloc.start()
    #Registramos tiempo en el que va a iniciar la función de Fibonacci
    start_time = time.time()
    #Se ejecuta la función
    fib_sequence = fibonacci(n)
    #Registramos el momento en el que se termina de ejecutar la función
    end_time = time.time()
    #Calculamos la diferencia de tiempo para saber cuánto tomó
    execution_time = end_time - start_time

    
    #Imprimimos los parámetros
    print("Secuencia de Fibonacci:", fib_sequence)
    print(f"Tiempo de ejecución: {execution_time:.15f} segundos")
    print(f"Uso de memoria:{tracemalloc.get_tracemalloc_memory()} bytes")
    #Una vez demostrado el uso de memoria podemos cerrar el registro.
    tracemalloc.stop()

if __name__ == "__main__":
    main()