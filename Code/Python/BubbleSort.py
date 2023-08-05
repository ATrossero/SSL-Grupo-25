import time
import resource

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Generar una lista de números desordenados
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    # Calcular el uso de memoria antes de ordenar
    initial_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # Medir el tiempo de ejecución
    start_time = time.time()

    # Ordenar la lista usando bubble sort
    bubble_sort(unsorted_list)

    # Calcular el tiempo de ejecución
    end_time = time.time()
    execution_time = end_time - start_time

    # Calcular el uso de memoria después de ordenar
    final_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    print("Lista ordenada:", unsorted_list)
    print("Tiempo de ejecución:", execution_time, "segundos")
    print("Uso de memoria inicial:", initial_memory/1024.0, "KB")
    print("Uso de memoria final:", final_memory/1024.0, "KB")
    print("Uso de memoria adicional durante la ejecución:", final_memory - initial_memory, "bytes")

if __name__ == "__main__":
    main()