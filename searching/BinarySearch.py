def binary_search(arr: list, ele: int) -> int:
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if ele < arr[mid]:
            high = mid - 1
        elif ele > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10))
