class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left=0
        right = 0
        max_count = 0
        my_dic = {}
        while right<n:
            my_dic[s[right]] = my_dic.get(s[right],0)+1
            while my_dic[s[right]]>1:
                my_dic[s[left]] -= 1
                if my_dic[s[left]]==0:
                    del my_dic[s[left]] 
                left+=1
            max_count = max(max_count,right-left+1)
            right+=1
        return max_count












        

        