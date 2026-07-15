class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if j <= i:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for r in range(n):
            matrix[r] = matrix[r][::-1]

