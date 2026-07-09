class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for string in s:
            if string.isalpha():
                lowered = string.lower()
                array.append(lowered)
            elif string.isdigit():
                array.append(string)
        
        reverse = array[::-1]

        if array == reverse:
            return True
        
        return False
