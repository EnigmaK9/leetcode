# ==============================================================================
# Creation Date: 2026-06-04
# Last Modified: 2026-06-04
# Description: This script finds the length of the very last word in a string.
# Author: enigmak9
# ==============================================================================


class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        # we start at the very last letter of the string and set our word counter to zero
        i, length = len(s) - 1, 0

        # this loop skips any empty spaces at the very end of the string by moving backward
        while s[i] == " ":
            # move one step to the left
            i -= 1

        # this loop counts the letters of the last word until it hits a space or the start of the text
        while i >= 0 and s[i] != " ":
            # we found a letter, so make our word count bigger by one
            length += 1
            # move one step to the left to check the next letter
            i -= 1

        # give back the total number of letters we counted for the last word
        return length
