class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined = []
        for i in matrix:
            combined += i
        l,r = 0,len(combined) - 1
        while l <= r:
            m = (l+r)//2
            if combined[m] == target:
                return True
            if target > combined[m]:
                l = m + 1
            else:
                r = m - 1
        return False
        