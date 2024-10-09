def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def quick_sort(arr: list, low: int, high: int) -> None:
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


if __name__ == '__main__':
    lst: list = [3, 23, 434, 12, 43, -12, -45]
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)
