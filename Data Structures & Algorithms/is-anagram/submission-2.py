class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCountS = {}
        charCountT = {}
        
        for char in s:
            charCountS[char] = 1 + charCountS.get(char, 0)
        for char in t:
            charCountT[char] = 1 + charCountT.get(char, 0)

        return charCountS == charCountT