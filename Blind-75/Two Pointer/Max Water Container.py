"""
Max Water Container
You are given an integer array heights where heights[i] represents the height of the i-th bar.


You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

"""


def maxArea(heights: list[int]) -> int:
    res = 0
    l, r = 0, len(heights) - 1
    while l < r:
        max_area = min(heights[l],heights[r]) * (r - l)
        res = max(max_area, res)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res


if __name__ == '__main__':
    print(maxArea(heights=[1, 7, 2, 5, 4, 7, 3, 6]))
