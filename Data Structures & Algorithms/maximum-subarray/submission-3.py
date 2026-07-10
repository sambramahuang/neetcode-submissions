class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingIn = nums[0]
        answer = nums[0]

        for x in nums[1:]:
            
            oldmax = maxEndingIn

            maxEndingIn = max(x, oldmax + x)

            answer = max(answer, maxEndingIn)

        return answer