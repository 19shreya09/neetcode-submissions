class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_countS = {}
        char_countT = {}

        for char in s:
            char_countS[char] = char_countS.get(char, 0) + 1

        for char in t:
            char_countT[char] = char_countT.get(char, 0) + 1

        return char_countS == char_countT
        