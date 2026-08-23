class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def target(value):
            subArray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > value:
                    subArray += 1
                    if subArray > k:
                        return False
                    curSum = num
            return True
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            mid = (l+r)//2
            if target(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

        