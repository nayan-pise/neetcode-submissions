class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_count = 0

        for num in num_set:

            # Start only if num is the beginning
            if num - 1 not in num_set:
                count = 1

                while num + 1 in num_set:
                    count += 1
                    num += 1

                max_count = max(max_count, count)

        return max_count