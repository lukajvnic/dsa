class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxval = 0
        i = 0
        j = 0
        
        seen = {}  # character: index

        while j < len(s):
            print(i,j)
            cur = s[j]

            if cur not in seen:
                seen[cur] = j
                maxval = max(maxval, j - i + 1)
                j += 1
            else:
                i = seen[cur] + 1
                seen2 = {}
                for k,v in seen.items():
                    if v >= i:
                        seen2[k] = v
                seen = seen2
        
        return maxval


sol = Solution()
print(sol.lengthOfLongestSubstring("zxyzxyz"))
