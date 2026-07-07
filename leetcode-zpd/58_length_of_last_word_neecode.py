"""
Creation Date: 2026-07-07
Last Modified: 2026-07-07
Description: This script defines a class to calculate the length of the last word in a given string by traversing it backward.
Author: enigmak9
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # start at the last index of the string
        # initialize length counter to zero
        i, length = len(s) - 1, 0

        # skip all trailing spaces at the end of the string
        while s[i] == " ":
            i -= 1

        # count the characters of the last word until a space or start of string is reached
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
