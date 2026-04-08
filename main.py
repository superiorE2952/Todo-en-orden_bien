import random
import time

from estructuras import LList
from ordenamientos import (
    bubble_sort,
    selection_sort,
    insertion_sort
)
from ordenamientos_2 import merge_sort, quick_sort
from visualizacion import graficar_complejidad
from utils import clear

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Graficar complejidad")

        op = input("Elige alguna opción: ")

        if op == "0":
            break
        elif op == "1":
            ejecutar_programa(bubble_sort)
        elif op == "2":
            ejecutar_programa(selection_sort)
        elif op == "3":
            ejecutar_programa(insertion_sort)
        elif op == "4":
            ejecutar_programa(merge_sort)
        elif op == "5":
            ejecutar_programa(quick_sort)
        elif op == "6":
            graficar_complejidad()     


            
            
def ejecutar_programa(algoritmo):
    try:
        size = int(input("Tamaño de lista (5-20): "))
        if size < 5 or size > 20:
            print("Fuera de rango")
            return
    except:
        print("Entrada inválida")
        return

    print("Velocidad:")
    print("1. Lento")
    print("2. Medio")
    print("3. Rápido")

    try:
        speed = int(input("Elige: "))
        if speed not in [1, 2, 3]:
            print("Velocidad inválida")
            return
    except:
        print("Entrada inválida")
        return

    ll = LList()

    for _ in range(size):
        ll.append(random.randint(1, 20))

    clear()
    print("Lista inicial:\n")
    ll.print_histogram()
    time.sleep(1)

    moves = algoritmo(ll, speed)

    clear()
    print("Lista ordenada:\n")
    ll.print_histogram()

    print(f"\nMovimientos: {moves}")            

if __name__ == "__main__":
    menu()    