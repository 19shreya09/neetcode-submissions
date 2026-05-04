class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""

        for s in strs:
            encoded += s + "/"
            
        return encoded


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        decoded = []
        inputs = s.split('/')
        for i in inputs[:-1]:
            decoded.append(i)
            
        return decoded
