import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for fre in freq:
            heapq.heappush(result, (-freq[fre], fre))

        for i in range(k):
            f,n = heapq.heappop(result)
            res.append(n)
            
        # while freq and k:
        #     maxNum = 0
        #     max = 0
        #     for fre in freq:
        #         if freq[fre] > max:
        #             max = freq[fre]
        #             maxNum = fre
        #     result.append(maxNum)
        #     freq.pop(maxNum)
        #     k -=1

        return res        

        
        