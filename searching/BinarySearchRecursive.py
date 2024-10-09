def binary_search(arr: list, ele: int, low: int, high: int) -> int:
    if low <= high:
        mid = (low + high) // 2
        if ele < arr[mid]:
            return binary_search(arr, ele, low, mid - 1)
        elif ele > arr[mid]:
            return binary_search(arr, ele, mid + 1, high)
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 6, 0, 9))
