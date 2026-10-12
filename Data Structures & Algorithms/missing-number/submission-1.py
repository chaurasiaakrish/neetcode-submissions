class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minn=min(nums)
        maxx=max(nums)
        for i in range(minn,len(nums)+1):
            if i in nums:
                continue
            else:
                return i   
        return 0         
        