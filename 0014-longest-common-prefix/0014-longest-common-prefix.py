class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0][0]
        counter = 0
        while True:
            for i in strs:
                if len(i) <= counter:
                    prefix = prefix[:-1]
                    return prefix
                if prefix[counter] == i[counter]:
                    pass
                else:                    
                    prefix = prefix[:-1]
                    return prefix
            counter += 1
            if counter == len(strs[0]):
                return prefix
            print(counter)
            prefix += strs[0][counter]