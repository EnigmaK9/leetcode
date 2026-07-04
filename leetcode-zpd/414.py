"""
Creation Date: July 4, 2026
Last Modified: July 4, 2026
Description: This script implements an optimized solution to find the third
             distinct maximum number in an integer array without full sorting.
Author: Carlos Ignacio Padilla Herrera
"""


class Solution(object):
    def thirdMax(self, nums):
        # convert to a set to remove all duplicates in a single pass
        unique_nums = set(nums)

        # if there are fewer than 3 unique numbers, return the maximum
        if len(unique_nums) < 3:
            return max(unique_nums)

        # remove the first maximum
        unique_nums.remove(max(unique_nums))
        # remove the second maximum
        unique_nums.remove(max(unique_nums))

        # the current maximum is now the third distinct maximum
        return max(unique_nums)
