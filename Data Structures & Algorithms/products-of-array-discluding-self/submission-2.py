class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodWithoutZero = 1
        countZero = 0

        for i in nums:
            prod *= i
            if i == 0:
                countZero += 1
            else:
                prodWithoutZero *= i
        arrayOfProds = []
        for i in nums:
            if i != 0:
                arrayOfProds.append(prod // i)
            elif countZero > 1:
                arrayOfProds.append(0)
            else:
                arrayOfProds.append(prodWithoutZero)
        
        return arrayOfProds
