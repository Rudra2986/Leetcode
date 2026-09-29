class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        result = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom :
            # 1. Top → Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])

            top += 1

            # 2. Top → Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

            right -= 1

            # 3. Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])

                bottom -= 1

            # 4. Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                left += 1
        
        return result