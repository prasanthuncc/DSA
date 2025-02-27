"""
LEETCODE: 347
Top K Elements in list
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""
from collections import Counter, defaultdict


def topKFrequent_easy(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    res = []
    i = 1
    for key, value in count.most_common():
        if i > k:
            break
        else:
            i += 1
            res.append(key)
    return res


def topKFrequent_bucket_sort(nums: list[int], k: int) -> list[int]:
    count = {}
    # creating a frequency array with list[list] where the list will have len(nums)+1 lists internally
    freq = [[] for i in range(len(nums) + 1)]
    # counting each number
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # say we get number 3 as count 5 then in the fifth index of frequency we add [3] and say we get number 9 five times now it will become [3,9] meaning appended
    for key, value in count.items():
        freq[value].append(key)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == '__main__':
    #print(topKFrequent_easy([1, 2, 2, 3, 3, 3], k=2))
    print(topKFrequent_bucket_sort([1, 2, 2, 3, 3, 3], k=2))
