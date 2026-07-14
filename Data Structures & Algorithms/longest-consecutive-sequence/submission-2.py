class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestfinal = 0
        clean = set()
        for num in nums:
            clean.add(num)

        for i in range(len(nums)):
            longest = 1
            if nums[i]-1 not in clean:
                current = nums[i]
                while (current+1) in clean:
                    longest +=1
                    current = current + 1
                if longest > longestfinal:
                    longestfinal = longest
        
        return longestfinal
