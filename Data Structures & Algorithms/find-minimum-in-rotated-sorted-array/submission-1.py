class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r ) // 2
        res = nums[mid]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            if nums[mid] < res:
                res = nums[mid]
            if nums[l] <= nums[mid]:
                l = mid +1
                mid = (l + r) // 2
            elif nums[mid] <= nums[r]:
                r = mid -1
                mid = (l + r) // 2

        return res