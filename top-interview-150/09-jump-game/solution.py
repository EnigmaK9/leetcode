class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        meta = n - 1

        for i in range(n -1, -1, -1):
            salto_maximo = nums [i]
            if i + salto_maximo >= meta:
                meta = i

        return meta == 0
