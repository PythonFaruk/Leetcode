roman = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        iold = 0
        num = 0
        for ii,i in enumerate(s):
            if ii == 0:
                iold = roman[i]
            else:
                if iold>=roman[i]:
                    num = num + iold
                elif iold<roman[i]:
                    num = num - iold
                iold = roman[i]
            print("Zahl: ",roman[i], " Zwischenergebnis: ", num)
        num = num + iold
        return num