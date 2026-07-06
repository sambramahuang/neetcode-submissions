class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outputlist = []
        dicty = {}
        
        for num in nums:
            if num in dicty:
                dicty[num] += 1
            else:
                dicty[num] = 1

        
        while len(outputlist) < k:
            for key in list(dicty.keys()):
                if dicty[key] == max(dicty.values()):
                    if len(outputlist) < k:
                        outputlist.append(key)
                        del dicty[key]

        return outputlist