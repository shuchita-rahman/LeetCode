class Solution:
    def singleNumber(self, nums: List[int]) -> int:                              #Suppose nums = [2,2,1] 
        for i in range(0, len(nums)):                                          
              if nums[i] not in nums[:i] and nums[i] not in nums[i+1:len(nums)]:
                     return nums[i]             
              
            
              
