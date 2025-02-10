class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        max_len = 1
        if len(s) <= 0:
            return 0
        for i in range(len(s)):
            res = s[i]
            for j in range(i+1 , len(s)):
                if s[j] not in res:
                    res = res + s[j]
                    max_len = max(max_len , len(res))
                
                else:
                    break
        return max_len


        