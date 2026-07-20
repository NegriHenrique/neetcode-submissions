# hash com a quantidade de cada letra distinta
# AAGAAAAAAAAABHJBHBHSDBFHJSDBFHJADDDDDDDDDD k=1



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        l, res = 0, 0

        frequency = {}
        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            
            most_frequency = max(frequency.values())

            while (r - l + 1) - most_frequency > k:
                frequency[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
        
        