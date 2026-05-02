class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        prefixint = 1
        suffixint = 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if j == len(nums) - 1:
                suffix.insert(0,1)
            else:
                suffix.insert(0, suffixint * nums[j+1])
                suffixint = suffix[0]
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefixint * nums[i-1])
                prefixint = prefix[-1]
        
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])

        
        print(prefix)
        print(suffix)
        return result
