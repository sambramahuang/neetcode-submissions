class Solution:

    def encode(self, strs: List[str]) -> str:
        laststring = ""
        for string in strs:
            laststring += str(len(string))+"#"+string
        return laststring

    def decode(self, s: str) -> List[str]:
        finallist = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i+1
                while j < len(s) and s[j] != "#":
                    j += 1
                length = int(s[i:j])
                word = s[j+1:j+1+length]
                finallist.append(word)
            i = j + 1 + length
        
        return finallist



