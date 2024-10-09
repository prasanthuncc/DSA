"""
LeetCode: 49
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from collections import defaultdict, Counter


def groupAnagrams_using_sorting(strs: list[str]) -> list[list[str]]:
    # not preferred as it takes O(m.nlogn) where m is no of words and nlogn is the time taken to sort each word
    result = defaultdict(list)
    for word in strs:
        result[tuple(sorted(word))].append(word)
    return list(result.values())


def groupAnagrams_using_dict(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for character in word:
            count[ord(character) - ord('a')] += 1
        result[tuple(count)].append(word)
    return result.values()


if __name__ == '__main__':
    print(groupAnagrams_using_sorting(["act", "pots", "tops", "cat", "stop", "hat"]))
    print(groupAnagrams_using_dict(["act", "pots", "tops", "cat", "stop", "hat"]))
