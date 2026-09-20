class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1

        while left <= right:
            head = left + ((right - left) // 2)
            if target < matrix[head // cols][head % cols]:
                right = head - 1
            elif target > matrix[head // cols][head % cols]:
                left = head + 1
            else:
                return True

        return False