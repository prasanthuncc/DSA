def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


if __name__ == '__main__':
    lst: list = [3, 23, 434, 12, 43, -12, -45]
    insertion_sort(lst)
    print(lst)
