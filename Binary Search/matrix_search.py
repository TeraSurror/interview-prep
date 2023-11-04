class Solution:
    def matrix_search(self, matrix, target):
        ROW, COL = len(matrix) - 1, len(matrix[0]) - 1
        start_row, end_row = 0, ROW
        start_col, end_col = 0, COL

        while start_row <= end_row and start_col <= end_col:
            mid_row = start_row + ((end_row - start_row) // 2)
            mid_col = start_col + ((end_col - start_col) // 2)
            if matrix[mid_row][mid_col] == target:
                return True
            elif target > matrix[mid_row][COL]:
                start_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                end_row = mid_row - 1
            else:
                if matrix[mid_row][mid_col] > target:
                    end_col = mid_col - 1
                else:
                    start_col = mid_col + 1

        return False
