# creation date: 2026-08-16
# last modified: 2026-08-16
# description: applies a 3x3 smoother to a 2d image by computing the floor average of all valid neighboring cells.
# author: carlos


class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        # get matrix dimensions
        m = len(img)
        n = len(img[0])

        # initialize the result matrix with zeros having dimensions m x n
        result = [[0] * n for _ in range(m)]

        # loop through each pixel in the image grid
        for r in range(m):
            for c in range(n):
                total = 0
                count = 0

                # inspect all 9 positions in the 3x3 square centered at (r, c)
                # dr and dc represent vertical and horizontal step offsets (-1, 0, 1)
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc

                        # ensure the target neighbor coordinates lie within grid boundaries
                        if 0 <= nr < m and 0 <= nc < n:
                            total += img[nr][nc]
                            count += 1

                # calculate floor average using integer division and store value
                result[r][c] = total // count

        return result
