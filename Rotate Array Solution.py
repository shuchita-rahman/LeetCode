class Solution:
    def rotate(self, nums: List[int], k: int):
     
        k= k % len(nums)
        if k == 0:
            return
        nums[:]= nums[-k:]+nums[:-k]
        
        
