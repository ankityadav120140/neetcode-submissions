class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    break
            else:
                ans.append(0)
        return ans