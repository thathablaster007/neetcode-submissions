class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u,d = 0,len(matrix)-1
        while u <= d:
            m1 = (u+d)//2
            l,r = 0,len(matrix[m1])-1
            while l <= r:
                m2 = (l + r)//2
                if matrix[m1][m2] == target:
                    return True
                elif target > matrix[m1][m2]:
                    l = m2 + 1
                else:
                    r = m2 - 1
            if matrix[m1][0] > target:
                d = m1 - 1
            else:
                u = m1 + 1
        return False
        