"""
creation date: 2026-08-28
last modified: 2026-08-28
description: check if the last character in a binary list is a 1-bit character
author: Carlos
"""

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        check if the last character must be a 1-bit character.
        we read bits from left to right using a pointer.
        """
        # start at the beginning of the list
        i = 0
        n = len(bits)

        # stop before the last element so we can inspect where we land
        while i < n - 1:
            if bits[i] == 0:
                # a '0' represents a single-bit character, so move forward by 1
                i += 1
            else:
                # a '1' starts a two-bit character (10 or 11), so move forward by 2
                i += 2

        # if pointer stops exactly at the last index, the last character is 1-bit
        return i == n - 1
