class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r,nums,target):
            if l > r:
                return -1
            n = (l+r)//2
            if nums[n] == target:
                return n
            elif target > nums[n]:
                return binary_search(n+1,r,nums,target)
            elif target < nums[n]:
                return binary_search(l,n-1,nums,target)
            
        return binary_search(0,len(nums)-1,nums,target)
        