# creation date: 2026-08-16
# last modified: 2026-08-16
# description: solution attempt at 661 image smoother
# author: enigmak9
class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        return [
            [
                sum(
                    img[x][y]
                    for x in range(max(0, r - 1), min(m, r + 2))
                    for y in range(max(0, c - 1), min(n, c + 2))
                )
                // ((min(m, r + 2) - max(0, r - 1)) * (min(n, c + 2) - max(0, c - 1)))
                for c in range(n)
            ]
            for r in range(m)
        ]
