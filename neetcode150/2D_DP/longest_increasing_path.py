from re import I
import re


class Solution:
    def longest_increasing_path(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        cache = dict()
        
        def traverse_path(row, col, prev_val):
            if row < 0 or row == ROWS or col < 0 or col == COLS or matrix[row][col] <= prev_val:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]

            result = 1
            result = max(result, 1 + traverse_path(row - 1, col, matrix[row][col]))
            result = max(result, 1 + traverse_path(row, col + 1, matrix[row][col]))
            result = max(result, 1 + traverse_path(row + 1, col, matrix[row][col]))
            result = max(result, 1 + traverse_path(row, col - 1, matrix[row][col]))
            cache[((row, col))] = result
            return result
            

        for i in range(ROWS):
            for j in range(COLS):
                traverse_path(i, j, -1)

        return max(cache.values())
