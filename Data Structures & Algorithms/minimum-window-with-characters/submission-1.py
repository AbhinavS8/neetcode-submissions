# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""

#         hash1 = Counter(t)
#         hash2 = {}
#         min_r = [0, float("inf")]

#         def compare(h1, h2):
#             for i in h1:
#                 if h2.get(i, 0) < h1[i]:
#                     return False
#             return True

#         l = 0

#         for r in range(len(s)):
#             hash2[s[r]] = hash2.get(s[r], 0) + 1

#             while compare(hash1, hash2):
#                 if (r - l + 1) < (min_r[1] - min_r[0]):
#                     min_r = [l, r]
#                 hash2[s[l]] -= 1
#                 l += 1

#         return s[min_r[0]:min_r[1] + 1] if min_r[1] != float("inf") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""