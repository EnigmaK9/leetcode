"""
Creation Date: 2026-08-17
Last Modified: 2026-08-17
Description: calculates the length of the longest continuous increasing subsequence (lcis) in a list of integers.
Author: enigmak9
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check if the input list is empty
        # an empty array contains no elements, so the streak length is zero
        if not nums:
            return 0

        # max_length stores the best streak record found across the entire list
        # since the array is not empty, the minimum possible valid answer is at least one
        max_length = 1

        # curr_length tracks the running length of the current strictly increasing streak
        # it starts at one to represent the first element in the current sequence
        curr_length = 1

        # iterate through the list starting at index one (the second element)
        # starting at index 1 allows us to safely inspect the previous element at index i - 1
        for i in range(1, len(nums)):
            # compare the current number with the immediately preceding number
            # we check for strict increase (greater than, not greater than or equal to)
            if nums[i] > nums[i - 1]:
                # the current increasing streak continues unbroken
                # increment the running streak counter by one
                curr_length += 1

                # update the global maximum streak if the current streak exceeds our previous record
                # max() evaluates both values and stores the larger one
                max_length = max(max_length, curr_length)
            else:
                # the sequence stopped increasing (the number is smaller or equal)
                # reset the running counter to one to start a new streak starting at nums[i]
                curr_length = 1

        # return the longest continuous increasing subsequence length recorded
        return max_length
