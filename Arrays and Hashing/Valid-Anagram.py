# dictionary.get(keyname, value)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of both strings are not same
        if len(s) != len(t):
            return False
       
        # initialize 2 hashmaps/dictionaries
        countS, countT = {}, {} 

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        
