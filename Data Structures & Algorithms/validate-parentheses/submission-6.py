class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        for a in s:
            if a == "[" or a == "{" or a == "(":
                stack1.append(a)
            else:
                if stack1:
                    top = stack1.pop()
                    if top == "[" and a != "]":
                        return False
                    elif top == "{" and a != "}":
                        return False
                    elif top == "(" and a != ")":
                        return False
                elif not stack1:
                    return False
            
        if stack1:
            return False
        
        return True
            
