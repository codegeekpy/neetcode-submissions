class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_s={}
        second_s={}
        for i in s:
            first_s[i] = first_s.get(i,0)+1

        for j in t:
            second_s[j] = second_s.get(j,0)+1
        
        for i in s:
            if i in t:
                second_s[i]-=1
        for j in t:
            if j in s:
                first_s[j]-=1
        
        for i in s:
            if first_s[i]!=0:
                return False
        for j in t:
            if second_s[j]!=0:
                return False
        return True
