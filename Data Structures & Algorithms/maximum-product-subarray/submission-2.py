class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnding = nums[0]
        minEnding = nums[0]
        answer = nums[0]

        for x in nums[1:]:
            oldMax = maxEnding

            maxEnding = max(x, oldMax * x, minEnding * x)   

            minEnding = min(x, oldMax * x, minEnding * x) 

            answer = max(answer, maxEnding) 

        return answer   



            