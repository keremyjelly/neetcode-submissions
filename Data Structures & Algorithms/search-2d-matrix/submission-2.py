class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1
        while bottom <= top:
            midrow = (bottom + top) // 2
            if matrix[midrow][0] < target:
                bottom = midrow + 1
            elif matrix[midrow][0] > target:
                top = midrow - 1
            else:
                return True

        if top < 0:              # target < matrix[0][0]
            return False

        row = matrix[top]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True
        return False