class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) -1

        leftMax , rightMax = height[l] , height[r]

        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax , height[l]) 
                res += leftMax - height[l] # not cheking for negative cuase it will nenver have -ve value as are updating the max before adding to res
            else:
                r -= 1
                rightMax = max(rightMax , height[r])
                res += rightMax - height[r]

        return res