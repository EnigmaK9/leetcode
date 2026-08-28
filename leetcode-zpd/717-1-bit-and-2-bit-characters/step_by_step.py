"""
creation date: 2026-08-28
last modified: 2026-08-28
description: step-by-step implementation of 1-bit and 2-bit characters problem
author: Carlos
"""

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # step 1: analyze constraints and define pointers
        # length of array is n, and the last bit bits[n - 1] is guaranteed to be 0.
        # we need to determine if this final 0 is standalone or part of a two-bit token.
        n = len(bits)
        i = 0

        # step 2: traverse tokens greedily from left to right
        # loop runs while we are strictly before the final element (n - 1).
        while i < n - 1:
            # step 3: inspect current bit to determine step size
            # if current bit is 0, it can only represent a one-bit character [0].
            # we increment the index by 1 step.
            if bits[i] == 0:
                i += 1
            # if current bit is 1, it must be the start of a two-bit character ([1, 0] or [1, 1]).
            # we consume both bits together by incrementing the index by 2 steps.
            else:
                i += 2

        # step 4: evaluate final pointer position
        # if the pointer lands exactly on index n - 1, the last element is an independent 1-bit character.
        # if the pointer jumped past the end to index n, the last 0 was consumed as part of a 2-bit character.
        return i == n - 1
