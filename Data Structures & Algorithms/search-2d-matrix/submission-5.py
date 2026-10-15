
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = len(matrix)
        b = len(matrix[0])

        r = -1
        for i in range(a):
            if matrix[i][0] <= target <= matrix[i][b - 1]:
                r = i
                break

        if r == -1:
            return False

        for j in range(b):
            if target == matrix[r][j]:
                return True

        return False
