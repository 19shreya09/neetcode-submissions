class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '/' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded = []
        i = 0
        while i < len(s):
            slash_index = s.find('/', i)
            length = int(s[i:slash_index])
            decoded.append(s[slash_index + 1: slash_index + 1 + length])
            i = slash_index + 1 + length

        return decoded









        
