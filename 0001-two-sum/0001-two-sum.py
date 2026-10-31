class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for xi,i in enumerate(nums):
            for xb,b in enumerate(nums):
                if(xi==xb):
                    pass
                elif (i+b == target):
                    erg = [xi, xb]
                    return erg