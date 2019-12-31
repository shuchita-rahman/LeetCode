class Solution:
    def rotate(self, nums: List[int], k: int):           #Critical test Case k=3 nums=[1,2]
                                                 
        k= k % len(nums)                                 #and test case k= 0 nums = anything   
        if k == 0:
            return
        nums[:]= nums[-k:]+nums[:-k]
        
        
