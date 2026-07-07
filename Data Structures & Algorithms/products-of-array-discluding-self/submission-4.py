class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finallist = []
        zerocount = 0
        product = 0
        zero = False
        for a in nums:
            if a == 0:
                zerocount += 1
        
        if zerocount == 0:
            product = 1
            for b in nums:
                product *= b

        elif zerocount == 1:
            product = 1
            for b in nums:
                if b != 0:
                    product *= b
        
        else:
            product = 0

        if zerocount >= 1:
            zero = True


        for i in range(0, len(nums)):
            if zero == True:
                if nums[i] != 0:
                    finallist.append(0)
                else:
                    finallist.append(product)
            if zero == False:
                finallist.append(int(product/nums[i]))

        return finallist
        

        
                