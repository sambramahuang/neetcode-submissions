class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noduplicates = set()
        for n in nums:
            if n in noduplicates:
                return True
            else:
                noduplicates.add(n)
        return False