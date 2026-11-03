class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        listnum = []
        for index, value in enumerate(digits):
            num = num + 10**(index)*digits[-(index+1)]
        num +=1
        for i in str(num):
            listnum.append(int(i))
        return listnum