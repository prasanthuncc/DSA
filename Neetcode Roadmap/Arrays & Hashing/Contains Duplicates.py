"""
LeetCode: 217
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
from typing import List


def has_duplicate(nums: List[int]) -> bool:
    hash_set = set()
    for i in nums:
        if i in hash_set:
            return True
        hash_set.add(i)
    return False


class Solution:
    pass


if __name__ == '__main__':
    print(has_duplicate(nums=[1, 2, 3, 4, 4, 5, 6, 7, 8]))
