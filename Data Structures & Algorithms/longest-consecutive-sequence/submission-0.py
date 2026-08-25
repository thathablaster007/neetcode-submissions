class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        sequence = 0
        length = 0
        for i in n:
            if (i - 1) not in n:
                length = 1
                while i + length in n:
                    length += 1
                sequence = max(length,sequence)
        return sequence

        