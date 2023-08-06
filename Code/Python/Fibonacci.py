import time
import tracemalloc

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
    n = int(input("Ingrese el valor de n para calcular los primeros n números de Fibonacci: "))
    tracemalloc.start()
    start_time = time.time()
    fib_sequence = fibonacci(n)
    end_time = time.time()

    

    print("Secuencia de Fibonacci:", fib_sequence)
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
    print(f"Uso de memoria:{tracemalloc.get_tracemalloc_memory()} bytes")
    tracemalloc.stop()

if __name__ == "__main__":
    main()