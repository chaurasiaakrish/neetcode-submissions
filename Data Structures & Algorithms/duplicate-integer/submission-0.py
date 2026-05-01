class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=set(nums)
        if len(i)<len(nums):
            return True
        else:
            return False    
        