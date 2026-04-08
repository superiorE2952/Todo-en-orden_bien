import matplotlib.pyplot as plt
import math
import random
import time

from ordenamientos import (
    bubble_sort_fast,
    selection_sort_fast,
    insertion_sort_fast
)

from ordenamientos_2 import (
    merge_sort_fast,
    quick_sort_fast
)

def graficar_complejidad():
    sizes = list(range(50, 401, 50))

    bubble_times = []
    selection_times = []
    insertion_times = []
    merge_times = []
    quick_times = []

    for n in sizes:
        base = [random.randint(1, 100) for _ in range(n)]

        
        arr = base.copy()
        start = time.time()
        bubble_sort_fast(arr)
        bubble_times.append(time.time() - start)

        
        arr = base.copy()
        start = time.time()
        selection_sort_fast(arr)
        selection_times.append(time.time() - start)

        
        arr = base.copy()
        start = time.time()
        insertion_sort_fast(arr)
        insertion_times.append(time.time() - start)

        
        arr = base.copy()
        start = time.time()
        merge_sort_fast(arr)
        merge_times.append(time.time() - start)

        
        arr = base.copy()
        start = time.time()
        quick_sort_fast(arr)
        quick_times.append(time.time() - start)

        print(f"Tamaño {n} completado")

    
    n2 = [x**2 for x in sizes]
    nlogn = [x * math.log2(x) for x in sizes]

    
    n2 = [x / max(n2) * max(bubble_times) for x in n2]
    nlogn = [x / max(nlogn) * max(merge_times) for x in nlogn]

    # Gráfica
    plt.plot(sizes, bubble_times, label="Bubble")
    plt.plot(sizes, selection_times, label="Selection")
    plt.plot(sizes, insertion_times, label="Insertion")
    plt.plot(sizes, merge_times, label="Merge")
    plt.plot(sizes, quick_times, label="Quick")

    plt.plot(sizes, n2, '--', label="O(n²)")
    plt.plot(sizes, nlogn, '--', label="O(n log n)")

    plt.xlabel("Tamaño de lista")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de algoritmos de ordenamiento")

    plt.legend()
    plt.show()




