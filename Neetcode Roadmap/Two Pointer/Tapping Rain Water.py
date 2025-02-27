"""Trapping Rain Water
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""


def trap(height: list[int]) -> int:
    size = len(height)
    left_max = [0] * size
    right_max = [0] * size
    l_wall = r_wall = 0
    res = 0
    for i in range(size):
        j = -i - 1
        left_max[i] = l_wall
        right_max[j] = r_wall
        l_wall = max(l_wall, height[i])
        r_wall = max(r_wall, height[j])
    for i in range(size):
        res += max(0, (min(left_max[i], right_max[i]) - height[i]))
    return res


if __name__ == '__main__':
    print(trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
    print(trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
