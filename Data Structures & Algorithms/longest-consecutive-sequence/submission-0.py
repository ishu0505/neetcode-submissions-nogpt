class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of a sequesnce
            # if has left neightbour then not start of a sequence
            if (n-1) not in numsSet:
                length = 0
                # if has right neightbour we increase the length by 1

                while(n+length) in numsSet:
                    length += 1
                longest = max(length , longest)
        return longest
        