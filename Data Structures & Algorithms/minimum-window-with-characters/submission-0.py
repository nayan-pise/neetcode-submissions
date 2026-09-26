class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        # Frequency of characters required from t
        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        window = {}

        # How many required characters are satisfied
        have = 0

        # Total unique characters we need to satisfy
        need = len(count)

        # Result
        res = ""
        resLen = float("inf")

        # Sliding window
        for right in range(len(s)):

            # Current character
            ch = s[right]

            # Add character to window
            window[ch] = window.get(ch, 0) + 1

            # Check if this character is required
            if ch in count:

                # Required frequency completed?
                if window[ch] == count[ch]:
                    have += 1

            # If all required characters are present
            while have == need:

                # Current window length
                windowLen = right - left + 1

                # Check if this is the smallest window
                if windowLen < resLen:
                    resLen = windowLen
                    res = s[left:right + 1]

                # Character we are removing
                leftChar = s[left]

                # Remove left character
                window[leftChar] -= 1

                # Did removing it make the window invalid?
                if leftChar in count:

                    if window[leftChar] < count[leftChar]:
                        have -= 1

                # Move left pointer
                left += 1

        return res