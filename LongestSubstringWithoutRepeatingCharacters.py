class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lindex={}
        maxlen=0
        strtindex=0
        for i in range(len(s)):
            if s[i] in lindex:
                    strtindex = max(strtindex, lindex[s[i]] + 1)
            maxlen = max(maxlen, i-strtindex + 1)
            lindex[s[i]] = i
        return maxlen
