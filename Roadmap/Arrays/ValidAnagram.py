class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        return sMap == tMap


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram(s="racecar", t="carrace"))
    print(sol.isAnagram(s="jar", t="jam"))
