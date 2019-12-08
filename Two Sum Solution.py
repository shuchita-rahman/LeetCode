class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
                                                                 #Lets think nums = [7,3,3,15] and target = 6
    sliceNums=[]                                
    result = []  

    for i in nums:
        indexOne = nums.index(i)                                  # when i = 3, indexOne = 1
        temp = target - i                                         # temp = 6 - 3 = 3
        sliceNums = nums[:indexOne] + nums[indexOne+1: len(nums)] # sliceNums = nums[:1] + nums[2:4]=[7,3,15]

        if temp in sliceNums:                                     # we will check if 3 in  sliceNums =[7,3,15] = true
            indexTwo = sliceNums.index(temp)                      # find index of 3 in sliceNums, indexTwo = 1
             if indexTwo >= indexOne:                             # We need to find out 3's index in num which is 2                      
                    indexTwo = indexTwo + 1                       # indexTwo = 1+1 = 2
            
            result.insert(0,indexOne)                             # result=[1]
            result.insert(1,indexTwo)                             # result= [1,2]
            return result                                         

