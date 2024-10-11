"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""


def encode(strs: list[str]) -> str:
    # Encode=ing in such a way like (count+#+string)+(count+#+string)
    encoded_str = ''
    for word in strs:
        encoded_str += str(len(word)) + '#' + word
    return encoded_str


def decode(s: str) -> list[str]:
    decoded_str = []
    numbers = [str(i) for i in range(0, 10)]
    i = 0
    while i < len(s):
        num = ''
        while s[i] in numbers:
            num += s[i]
            i += 1
        count = int(num)
        i += 1
        j = 0
        decoded_word = ''
        while j < count:
            decoded_word += s[i]
            i += 1
            j += 1
        decoded_str.append(decoded_word)

    return decoded_str


def decode_neetcode(s: str) -> list[str]:
    decoded_str = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        count = int(s[i:j])
        i = j + 1
        j = i + count
        decoded_str.append(s[i:j])
        i = j
    return decoded_str


if __name__ == '__main__':
    encoded = encode(['cat', 'rat', 'sample'])
    print(encoded)
    decoded = decode_neetcode(encoded)
    print(decoded)
