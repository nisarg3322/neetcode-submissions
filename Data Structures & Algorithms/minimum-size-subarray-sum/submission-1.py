class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minVal = len(nums) + 1
        total = 0

        L = 0

        for R in range(len(nums)):
            total += nums[R]
            print("total:", total)

            if total >= target:
                minVal = min(minVal , R-L+1)
                while total >= target:
                    total -= nums[L]
                    L += 1
                    if total >= target:
                        minVal = min(minVal , R-L+1)

            
        

        return 0 if minVal == len(nums) + 1 else minVal
        
        