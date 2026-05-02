import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first == second:
                continue
            second = abs(second - first)
            heapq.heappush(heap, -second)
                
        if len(heap):
            return -heapq.heappop(heap)
        else:
            return 0