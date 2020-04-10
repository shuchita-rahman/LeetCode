class Solution:
    def reverse(self, x: int):
        flag = 0
        minus = "-"
        
        if x < 0:
            flag = 1
            x = x * -1
        
        result= str(x)
        result = ''.join(reversed(result))
        x = int(result)

        if flag == 1:
             x = x * -1
        if x > 2147483647 or x < -2147483647:
            return 0
        return x
          
       
       
