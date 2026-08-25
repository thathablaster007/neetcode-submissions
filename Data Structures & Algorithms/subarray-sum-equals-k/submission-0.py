class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        hashmap = {0:1}
        for i in nums:
            currSum += i
            diff = currSum - k
            res += hashmap.get(diff,0)
            hashmap[currSum] = hashmap.get(currSum,0) + 1
        return res
        