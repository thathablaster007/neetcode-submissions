class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums4 = nums1[0:m]
        nums3 = []
        i = j = 0
        while i < len(nums4) and j < len(nums2):
            if nums4[i] < nums2[j]:
                nums3.append(nums4[i])
                i += 1
            elif nums4[i] > nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums4[i])
                nums3.append(nums2[j])
                i += 1
                j += 1
        if i != len(nums4):
            nums3.extend(nums4[i:])
        elif j != len(nums2):
            nums3.extend(nums2[j:])
        
        nums1[:] = nums3
        