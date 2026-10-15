class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a= len(matrix)
        b= len(matrix[0])
        for i in range(a):
            for j in range(b):
                if target==matrix[i][j]:
                    return True
        return False
