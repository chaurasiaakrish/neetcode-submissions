class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr=0
        low=0
        high=len(nums)-1
        while curr<=high:
            if nums[curr]==2:
                nums[curr],nums[high]=nums[high],nums[curr]
                high-=1
            elif nums[curr]==1:
                curr+=1
            else:
                nums[curr],nums[low]=nums[low],nums[curr]
                low+=1
                curr+=1
