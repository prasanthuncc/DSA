def selection_sort(arr):
    for i in range(0, len(arr)):
        curr_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min_index]:
                curr_min_index = j
        arr[curr_min_index], arr[i] = arr[i], arr[curr_min_index],


if __name__ == '__main__':
    lst: list = [3, 23, 434, 12, 43, -12, -45]
    selection_sort(lst)
    print(lst)
