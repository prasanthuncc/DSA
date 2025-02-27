"""
Three Integer Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i, v in enumerate(nums):
        if v > 0:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = v + nums[l] + nums[r]
            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0, 0, 0]))
