class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j <= i:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]

