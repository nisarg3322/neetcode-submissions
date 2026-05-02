class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        mid = (l+r) // 2
        row = 0
        # first binary search the rows
        while l <= r:
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                row = matrix[mid]
                break
            if target < matrix[mid][0]:
                r = mid - 1
                mid = (l + r) // 2
            elif target > matrix[mid][len(matrix[mid])-1]:
                l = mid + 1
                mid = (l + r) // 2

        if row == 0:
            return False
        # second binary search in that row
        l = 0
        r = len(row) - 1
        mid = (l+r) // 2

        while l<=r:
            if target == row[mid]:
                return True
            if target < row[mid]:
                r = mid -1
                mid = (l+r) // 2
            elif target > row[mid]:
                l = mid +1
                mid = (l+r) // 2

        return False 