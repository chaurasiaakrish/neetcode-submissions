class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        if len(heap)==1:
            return -heap[0]
        elif len(heap)==0:
            return 0
        else:    
            while len(heap)>=2:
                x=-heapq.heappop(heap)
                y=-heapq.heappop(heap)
                if x==y:
                    continue
                elif x>y:
                    num=x-y
                    heapq.heappush(heap,-num)
        if len(heap)==1:
            return -heap[0]
        elif len(heap)==0:
            return 0       

        