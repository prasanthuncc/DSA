from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += + 1
            res_map[tuple(count)].append(s)
        return res_map.values()


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))
