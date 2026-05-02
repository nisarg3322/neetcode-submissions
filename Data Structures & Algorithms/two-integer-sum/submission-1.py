class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i ,  num in enumerate(nums):
            hashmap[num] = i
        

        for i ,  num in enumerate(nums):
            cont = target - num
            if cont in hashmap and hashmap[cont] != i:
                return [i, hashmap[cont]]
        
        return None