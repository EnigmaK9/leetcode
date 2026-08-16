# creation date: 2026-08-16
# last modified: 2026-08-16
# description: top runtime image smoother using separable 1d horizontal and vertical sliding window sums.
# author: enigmak9
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])

        # calculate horizontal neighbor counts for each column
        # single column grids have weight 1, boundary edges have weight 2, and inner cells have weight 3
        if n == 1:
            col_weights = [1]
        elif n == 2:
            col_weights = [2, 2]
        else:
            col_weights = [2] + [3] * (n - 2) + [2]

        # calculate vertical neighbor counts for each row
        if m == 1:
            row_weights = [1]
        elif m == 2:
            row_weights = [2, 2]
        else:
            row_weights = [2] + [3] * (m - 2) + [2]

        # step 1: precalculate 1d horizontal sums for each row
        # this separates 2d convolution into two 1d passes, eliminating redundant 3x3 loop iterations
        row_sums = []
        for r in range(m):
            row = img[r]
            if n == 1:
                row_sums.append([row[0]])
            elif n == 2:
                s = row[0] + row[1]
                row_sums.append([s, s])
            else:
                curr_sum = [row[0] + row[1]]
                for c in range(1, n - 1):
                    curr_sum.append(row[c - 1] + row[c] + row[c + 1])
                curr_sum.append(row[n - 2] + row[n - 1])
                row_sums.append(curr_sum)

        # step 2: sum along columns using the precomputed row sums and divide by total cell count
        result = [[0] * n for _ in range(m)]
        for r in range(m):
            rw = row_weights[r]
            res_row = result[r]

            # select rows to sum based on vertical position
            if m == 1:
                r0 = row_sums[0]
                for c in range(n):
                    res_row[c] = r0[c] // (rw * col_weights[c])
            elif m == 2:
                r0, r1 = row_sums[0], row_sums[1]
                for c in range(n):
                    res_row[c] = (r0[c] + r1[c]) // (rw * col_weights[c])
            else:
                if r == 0:
                    r0, r1 = row_sums[0], row_sums[1]
                    for c in range(n):
                        res_row[c] = (r0[c] + r1[c]) // (rw * col_weights[c])
                elif r == m - 1:
                    r0, r1 = row_sums[m - 2], row_sums[m - 1]
                    for c in range(n):
                        res_row[c] = (r0[c] + r1[c]) // (rw * col_weights[c])
                else:
                    r0, r1, r2 = row_sums[r - 1], row_sums[r], row_sums[r + 1]
                    for c in range(n):
                        res_row[c] = (r0[c] + r1[c] + r2[c]) // (rw * col_weights[c])

        return result
