class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(k):
            res=-heapq.heappop(heap)
        return res        
        