from utils import clear, delay

def bubble_sort(ll, speed):
    moves = 0

    for _ in range(ll.size):
        current = ll.head

        while current and current.next:
            if current.value > current.next.value:
                
                current.value, current.next.value = current.next.value, current.value
                moves += 1

                clear()
                ll.print_histogram()
                delay(speed)

            current = current.next

    return moves   
def bubble_sort_fast(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]               


def selection_sort(ll, speed):
    moves = 0
    i = ll.head

    while i:
        min_node = i
        j = i.next

        while j:
            if j.value < min_node.value:
                min_node = j
            j = j.next

        if min_node != i:
            i.value, min_node.value = min_node.value, i.value
            moves += 1

            clear()
            ll.print_histogram()
            delay(speed)

        i = i.next

    return moves
def selection_sort_fast(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    


def insertion_sort(ll, speed):
    if not ll.head:
        return 0

    moves = 0
    current = ll.head.next

    while current:
        key = current.value
        prev = ll.head

        while prev != current:
            if prev.value > key:
                prev.value, key = key, prev.value
                moves += 1

                clear()
                ll.print_histogram()
                delay(speed)

            prev = prev.next

        current.value = key
        current = current.next

    return moves


def insertion_sort_fast(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



