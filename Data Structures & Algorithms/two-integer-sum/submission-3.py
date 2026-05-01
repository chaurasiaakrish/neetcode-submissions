class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while(i<j):
            if abs(nums[i]+nums[j])==target:
                return [i,j]
            elif abs(nums[i]+nums[j])>target:
                j-=1
            elif abs(nums[i]+nums[j])<target:
                i+=1        
        