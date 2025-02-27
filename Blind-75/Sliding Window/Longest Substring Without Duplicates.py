"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""


def lengthOfLongestSubstring(s: str) -> int:
    pos = 0
    initial_char = s[0]
    res = 0
    while pos < len(s):
        res = s.find(initial_char, pos + 1, len(s))
        if res != -1:
            res += 1
            pos = res
        else:
            break
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring("zxyzxyz"))
    print(lengthOfLongestSubstring("xxxx"))
    print(lengthOfLongestSubstring("pwwkew"))
