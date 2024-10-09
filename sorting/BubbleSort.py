def bubble_sort(arr):
    swapped = True
    i = 0
    while swapped:
        swapped = False
        for j in range(i + 1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True


if __name__ == '__main__':
    lst: list = [3, 23, 434, 12, 43, -12, -45]
    bubble_sort(lst)
    print(lst)
