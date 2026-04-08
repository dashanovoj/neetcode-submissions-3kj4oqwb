class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low, row_high = 0, len(matrix) - 1

        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            L, R = 0, len(matrix[row_mid]) - 1

            while L <= R:
                mid = (L + R) // 2

                if target > matrix[row_mid][mid]:
                    L = mid + 1
                elif target < matrix[row_mid][mid]:
                    R = mid - 1
                else:
                    return True
            
            if target > matrix[row_mid][-1]:
                row_low = row_mid + 1
            elif target < matrix[row_mid][-1]:
                row_high = row_mid - 1

        return False
        