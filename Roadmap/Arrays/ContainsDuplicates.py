class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        numsSet = set()
        for i in range(len(nums)):
            if nums[i] in numsSet:
                return True
            numsSet.add(nums[i])
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.hasDuplicate(nums=[1, 2, 3, 3]))
    print(sol.hasDuplicate(nums=[1, 2, 3, 4]))
