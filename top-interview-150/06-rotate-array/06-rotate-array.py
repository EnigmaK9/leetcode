class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.

        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Find the length of the array
        n = len(nums)

        # Ensure k is within the bounds of the array length
        k = k % n

        # Define a helper function to reverse a portion of the array in-place
        def reverse(start, end):
            while start < end:
                # Swap the elements at index start and end
                nums[start], nums[end] = nums[end], nums[start]
                # Move towards the center
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the remaining elements
        reverse(k, n - 1)

# Example usage
solution = Solution()

nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
solution.rotate(nums1, k1)
print(nums1)  # Output should be [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
solution.rotate(nums2, k2)
print(nums2)  # Output should be [3, 99, -1, -100]

