class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l):
            j = i + 1
            while j < l-1 and numbers[i] + numbers[j] < target:
                j += 1
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            
