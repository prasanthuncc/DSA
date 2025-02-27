def findFirstBeautifulMoment(n, m, k, paint):
    grid = [[False] * m for _ in range(n)]

    def has_k_square(i, j):
        if i + 1 < k or j + 1 < k:
            return False
        for x in range(i - k + 1, i + 1):
            for y in range(j - k + 1, j + 1):
                if not grid[x][y]:
                    return False
        return True

    for minute, (x, y) in enumerate(paint):
        grid[x - 1][y - 1] = True
        for i in range(n):
            for j in range(m):
                if has_k_square(i, j):
                    return minute + 1
    return -1


if __name__ == '__main__':
    # Example usage:
    n = 3
    m = 3
    k = 3
    paint = [
        [3, 2],
        [2, 3],
        [1, 2],
        [2, 1],
        [3, 3],
        [3, 1],
        [1, 1],
        [1, 3],
        [2, 2]
    ]
    # n = 2
    # m = 1
    # k = 1
    # paint = [
    #     [2, 1],
    #     [1, 1]
    # ]

    print(findFirstBeautifulMoment(n, m, k, paint))  # Output: 9
