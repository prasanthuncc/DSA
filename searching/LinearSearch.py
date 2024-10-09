def linear_search(arr: list, ele: int) -> int:
    for i, v in enumerate(arr):
        if v == ele:
            return i
    return -1


if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 8))
