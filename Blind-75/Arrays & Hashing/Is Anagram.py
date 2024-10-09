"""
LeetCode: 242
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""
from collections import Counter


# solution-1
def isAnagram_using_counter_elaborated(s: str, t: str) -> bool:
    s_counter = Counter(s)
    t_counter = Counter(t)

    if sum(s_counter.values()) == sum(t_counter.values()):
        for k, v in s_counter.items():
            t_value = t_counter[k]
            if t_value != v:
                return False
        return True
    return False


# solution-2
def isAnagram_using_counter_easy(s: str, t: str) -> bool:
    # solution-1 using counter-- with counters we can solve this two ways
    s_counter = Counter(s)
    t_counter = Counter(t)
    return s_counter == t_counter


# solution-3 using dict
def isAnagram_using_dict(s: str, t: str) -> bool:
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
    for i in range(len(t)):
        countT[t[i]] = countT.get(t[i], 0) + 1
    if len(countS.values()) != len(countT.values()):
        return False
    for key in countS:
        if countS[key] != countT.get(key, 0):
            return False
    return True


if __name__ == '__main__':
    print(isAnagram_using_counter_easy("racecar", "carrace"))
    print(isAnagram_using_counter_elaborated("racecar", "carrace"))
    print(isAnagram_using_dict("anagram", "nagaram"))
