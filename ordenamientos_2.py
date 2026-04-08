from utils import clear, delay

def merge_sort(ll, speed):
    arr = ll.to_list()
    moves = [0]  

    def merge_sort_rec(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort_rec(arr[:mid])
        right = merge_sort_rec(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

            moves[0] += 1
            ll.update_from_list(result + left[i:] + right[j:])
            clear()
            ll.print_histogram()
            delay(speed)

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = merge_sort_rec(arr)
    ll.update_from_list(sorted_arr)

    return moves[0]


def merge_sort_fast(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_fast(arr[:mid])
    right = merge_sort_fast(arr[mid:])

    return merge_fast(left, right)


def merge_fast(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result





def quick_sort(ll, speed):
    arr = ll.to_list()
    moves = [0]

    def quicksort_rec(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_rec(arr, low, pi - 1)
            quicksort_rec(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                moves[0] += 1

                ll.update_from_list(arr)
                clear()
                ll.print_histogram()
                delay(speed)

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        moves[0] += 1

        ll.update_from_list(arr)
        clear()
        ll.print_histogram()
        delay(speed)

        return i + 1

    quicksort_rec(arr, 0, len(arr) - 1)
    return moves[0]


def quick_sort_fast(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_fast(left) + middle + quick_sort_fast(right)
