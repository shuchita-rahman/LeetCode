class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         for i in nums:                      #Suppose, nums =[0,25,4,0,5]
            if i == 0:                       #Check if i is equal to 0 
                nums.remove(i)               #than remove i from the list. Now nums = [25,4,0,5]
                nums.append(i)               #Push 0 at the end of the list. Now nums =[25,4,0,5,0]
             
             
