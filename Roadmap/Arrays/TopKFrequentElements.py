from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_map = Counter(nums)
        count = [[] for i in range(len(nums) + 1)]
        res = []
        for key, value in nums_map.items():
            count[value].append(key)
        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                for j in count[i]:
                    res.append(j)
                    if len(res) >= k:
                        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 100], k=2))
