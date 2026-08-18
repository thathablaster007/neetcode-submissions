class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        correct_position = len(nums)
        while l <= r:
            n = (l + r) // 2
            if nums[n] == target:
                return n
            if nums[n] > target:
                correct_position = n
                r = n - 1
            else:
                l = n + 1
        return correct_position
        