 # Suppose nums = [1,3,2,4]
 # sorted(nums) = [1,2,3,4].Now there are two pair (1,2),(3,4) 
 # nums[::2] = [1,3]
 # sum = 1 + 3 = 4
 
 def arrayPairSum(nums):
        return sum(sorted(nums)[::2]) 
        
        
        
