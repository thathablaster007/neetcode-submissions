class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = set(nums)
        nums2 = []
        for i in nums:
            if i in nums1:
                nums2.append(i)
                nums1.remove(i)
        nums[:] = nums2
        return len(nums2)
        