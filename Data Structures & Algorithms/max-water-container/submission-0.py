class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = 0
        while left < right :
            area = min(heights[left],heights[right])*(right-left)
            best = max(best,area)
            if heights[right]<heights[left]:
                right-=1
            else :
                left+=1
        return best



        