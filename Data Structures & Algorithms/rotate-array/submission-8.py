class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        while i < k:
            nums.reverse()
            nums.append(0)
            nums.reverse()
            popped = nums.pop()
            nums[0] = popped
            i += 1


        

        