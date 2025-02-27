from base64 import encode, decode


class Solution:

    def encode(self, strs: list[str]) -> str:
        enc_str = ''
        for s in strs:
            enc_str += ''.join(str(len(s)) + '#' + s)
        return enc_str

    def decode(self, s: str) -> list[str]:
        decoded_string_list = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            j = i + num
            decoded_string_list.append(s[i:j])
            i = j
        return decoded_string_list


if __name__ == '__main__':
    sol = Solution()
    encoded_string = sol.encode(["neet", "code", "love", "you"])
    print(encoded_string)
    print(sol.decode(encoded_string))
    print()
    encoded_string_2 = sol.encode([""])
    print(encoded_string_2)
    print(sol.decode(encoded_string_2))


 # Output: 'bcdef'
