class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s1=[]
        result = []  
        for i in nums:
            indexOne = nums.index(i)

            temp = target - i
            s1 = nums[:indexOne] + nums[indexOne+1: len(nums)]
            if temp in s1:
                indexTwo = s1.index(temp)
                if indexTwo >= indexOne:
                        indexTwo = indexTwo +1
                result.insert(0,indexOne)
                result.insert(1,indexTwo)
                return result
