class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum,maxSub = 0,nums[0]
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSub = max(maxSub,currSum)
        return maxSub