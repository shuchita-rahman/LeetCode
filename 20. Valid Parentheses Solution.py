class Solution:
    def isValid(self, s: str) -> bool:
        queue =[]
        
        for i in s:
                if i != ")"and i != "}" and i !="]":
                     queue.append(i)
                else:
                    if len(queue) == 0:
                        return False
                    check = queue.pop()
                    if i == ')' and check !='(' or i == '}' and check !='{' or i == ']' and check !='[':
                        return False

        if len(queue) == 0:
                return True
                
