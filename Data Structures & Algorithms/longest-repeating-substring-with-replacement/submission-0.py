class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = 0
        max_freq = 0
        max_length = 0
        my_dic = {}

        for right in range(n):
            my_dic[s[right]] = my_dic.get(s[right], 0) + 1

            max_freq = max(max_freq, my_dic[s[right]])

            while (right - left + 1) - max_freq > k:
                my_dic[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
                
            

        
        