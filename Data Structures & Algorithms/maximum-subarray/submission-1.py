class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEnding = nums[0]
        answer = nums[0]

        for x in nums[1:]:
            
            oldmax = maxEnding

            maxEnding = max(x, oldmax + x)

            answer = max(answer, maxEnding)

        return answer