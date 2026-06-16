from collections import Counter
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #how to identify which element to check next?
        #store it maybe
        #store each elements longest? NOT OPTIMAL
        #replacing for most frequent element is always the case,
        # so find the most frequent elem and set that

        # if len(s)==0:
        #     return 0
        
        # if len(s)==1:
        #     return 1

        # next_elem_ind=0
        # curr_elem=s[0]
        # hashset={curr_elem:0}
        # repcnt=0
        # cnt=0
        # max_s=0

        # for i in s:
        #     if i==curr_elem:
        #         hashset[i]+=1
        #         repcnt+=1
        #     else:

        #         hashset[i]=1

        
        # cts=Counter(s)
        # max_elem,max_val="",0
        # for i in cts:
        #     if cts[i]>max_val:
        #         max_elem=i
        
        l=0
        maxf=0
        # repcnt=0
        count={}
        res=0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


        # print(i,max_elem)
        # for i in s:
        #     print(repcnt,cnt)
        #     if i==max_elem:
        #         repcnt+=1
        #     else:
        #         cnt+=1
        #         if cnt==k:
        #             max_s=max(repcnt+k,max_s)
        #             repcnt=0

        # max_s=max(repcnt+k,max_s)

        # return max_s



