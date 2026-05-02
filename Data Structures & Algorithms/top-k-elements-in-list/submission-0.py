
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        while freq and k:
            maxNum = 0
            max = 0
            for fre in freq:
                if freq[fre] > max:
                    max = freq[fre]
                    maxNum = fre
            result.append(maxNum)
            freq.pop(maxNum)
            k -=1

        return result        

        
        