class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        leftWall = [0] * l
        rightWall = [0] * l

        maxLeftWall = 0
        maxRightWall = 0

        for i in range(l):
            maxLeftWall = max(height[i], maxLeftWall)
            leftWall[i] = maxLeftWall
        
        for i in range(l-1,-1,-1):
            maxRightWall = max(height[i], maxRightWall)
            rightWall[i] = maxRightWall
        
        res = 0

        for i in range(l):
            res += (min(leftWall[i], rightWall[i]) - height[i])
        
        return res