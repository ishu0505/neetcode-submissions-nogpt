class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prefMap:
                return [prefMap[diff],  i]
            prefMap[n] = i
        return
        