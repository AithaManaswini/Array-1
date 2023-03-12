# time complexity - O(mn)
# space complexity - O(m + n)
#  Did this code successfully run on Leetcode :yes
# Three line explanation of solution in plain english
# loop through the row, left to right on first row, top to bottom in last column
# right to left in last row and bottom to top in first column and increase rowstart,columnstart by one,
# row end,column end by 1 and loop out when the length of result is equal to no of elements in matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs = 0
        re = len(matrix) -1
        cs = 0
        ce = len(matrix[0]) - 1
        count = 0
        arr = []
        while count < len(matrix)*len(matrix[0]):
            for j in range(cs,ce+1):
                arr.append(matrix[rs][j])
                count+=1
            rs += 1
            if count == len(matrix)*len(matrix[0]):
                break
            for i in range(rs, re+1):
                arr.append(matrix[i][ce])
                count+=1
            ce-=1
            if count == len(matrix)*len(matrix[0]):
                break
            for j in range(ce, cs-1,-1):
                arr.append(matrix[re][j])
                count+=1
            re-=1
            if count == len(matrix)*len(matrix[0]):
                break
            for i in range(re,rs-1,-1):
                arr.append(matrix[i][cs])
                count+=1
            cs+=1
            if count == len(matrix)*len(matrix[0]):
                break
        return arr


