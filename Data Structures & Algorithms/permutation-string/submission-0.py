class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}

        # Frequency of s1
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        window = {}

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Keep window size equal to s1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # Check if window is a permutation
            if window == count:
                return True

        return False