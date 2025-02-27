class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums_map = {}
        for i in range(len(nums)):
            component = target - nums[i]
            if component in nums_map:
                return [nums_map.get(component), i]
            nums_map[nums[i]] = i


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[3, 4, 5, 6], target=7))
    print(sol.twoSum([4, 5, 6], target=10))
    print(sol.twoSum(nums=[5, 5], target=10))
    print(sol.twoSum(nums=[1, 6, 3, 2], target=4))
