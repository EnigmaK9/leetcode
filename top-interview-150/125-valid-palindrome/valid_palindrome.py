"""
creation date
last modified: 2026-05-15
description: valid palindrome solution got from neetcode
author: enigmak9
"""
"""
Removing the useless character and checking if the strings are equal
Multiple ways to check if something is a palindrome
left pointer right pointer until they meet
that's how we know we can stop
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
            newStr == newStr[::-1]
