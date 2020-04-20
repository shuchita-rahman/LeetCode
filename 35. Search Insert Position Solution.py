class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0,len(nums)-1
        
        if target < nums[low]:
            return 0
        elif target > nums[high]:
            return high+1
        
        while low <= high:
            mid = int((low + high) / 2)
            
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low
