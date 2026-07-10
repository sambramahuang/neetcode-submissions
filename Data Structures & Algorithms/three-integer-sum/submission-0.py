class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = nums.copy()
        sortednums.sort()
        #[-4,-1,-1,0,1,2]
        finallist = []
        for i in range(0, len(sortednums)):
            left = i + 1
            right = len(sortednums)-1

            while right>left:
                total = sortednums[i]+sortednums[left]+sortednums[right]
                if total == 0:
                    triplets = [sortednums[i], sortednums[left], sortednums[right]]
                    if triplets not in finallist:
                        finallist.append(triplets)
                    left += 1
                    right -= 1
                elif total > 0:
                    right -=1
                else:
                    left +=1


        return finallist



        
                    

            