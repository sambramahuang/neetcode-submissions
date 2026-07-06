class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finallist = []
        dicty = {}
        for string in strs:
            stringsorted = str(sorted(string))
            if stringsorted not in dicty:
                dicty[stringsorted] = [string]
            else:
                dicty[stringsorted].append(string)
            
        for value in dicty.values():
            finallist.append(value)

        return finallist


