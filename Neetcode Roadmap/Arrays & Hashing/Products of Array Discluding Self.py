"""Products of Array Discluding Self
LEETCODE :238
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 2
"""
from itertools import product


def productExceptSelf(nums: list[int]) -> list[int]:
    # This will work with the division operator //...
    zero_count = zero_index = 0
    p = 1
    size = len(nums)
    res = [0] * size
    for i in range(size):
        if nums[i] != 0:
            p *= nums[i]
        else:
            zero_count += 1
            zero_index = i
            if zero_count >= 2:
                return res

    if zero_count:
        res[zero_index] = p
    else:
        for i in range(len(nums)):
            res[i] = p // nums[i]
    return res


# If the interviewer ask to not use the division operator
def productExceptSelf_optimal(nums: list[int]) -> list[int]:
    size = len(nums)
    res = [1] * size
    prefix_product = 1
    postfix_product = 1
    for i in range(size):
        res[i] = prefix_product
        prefix_product *= nums[i]
    for i in range(size - 1, -1, -1):
        res[i] *= postfix_product
        postfix_product *= nums[i]
    return res


if __name__ == '__main__':
    # print(productExceptSelf([-1, 0, 1, 2, 3]))
    # print(productExceptSelf([0, 0]))
    # print(productExceptSelf([1, 2, 4, 6]))
    # print("Optimal-Solution")
    # print(productExceptSelf_optimal([-1, 0, 1, 2, 3]))
    # print(productExceptSelf_optimal([0, 0]))
    # print(productExceptSelf_optimal([1, 2, 4, 6]))
    print(productExceptSelf_optimal([1, 2, 3, 4, 5]))
