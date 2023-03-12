# time complexity - O(mn)
# space complexity - O(m + n)
#  Did this code successfully run on Leetcode :yes
# Three line explanation of solution in plain english
# all the diagonal elements have the sum of their indices same.So, group them
# by sum of indices and loop over the dictionary to find the result array
# traverse reverse or in the same direction depending on the whether sum is even or odd
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        col = len(mat[0])
        d = {}
        for i in range(rows):
            for j in range(col):
                if i+j in d:
                    d[i+j].append(mat[i][j])
                else:
                    d[i+j]=[mat[i][j]]
        arr = []
        for i,j in d.items():
            if i%2!=0:
                arr.extend(j)
            else:
                j.reverse()
                arr.extend(j)
        return arr

        