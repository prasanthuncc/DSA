"""

LEETCODE: 128
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


"""


def longestConsecutive(nums: list[int]) -> int:
    hashSet = set(nums)
    max_count = 0
    for i in nums:
        if i - 1 not in hashSet:
            print(f'turn of {i}')
            count = 1
            while (i + 1) in hashSet:
                count += 1
                i += 1
            if count > max_count:
                max_count = count
    return max_count


if __name__ == '__main__':
    print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
    print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
