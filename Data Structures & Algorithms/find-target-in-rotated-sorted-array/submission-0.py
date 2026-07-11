class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        

        while right>=left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                #left is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid+1

            elif nums[right] >= nums[mid]:
                if nums[right] >= target > nums[mid]:
                    left = mid
                else:
                    right = mid-1

        return -1

