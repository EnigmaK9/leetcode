class Solution:
    def isPalindrome(self, s:str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[1].lower() != s[r].lower():
                return False
    def alphaNum(self, c):
        (ord('A') <= ord(c) <= ord('Z') or
        (ord('A') <= ord(c) <= ord('Z') or )

