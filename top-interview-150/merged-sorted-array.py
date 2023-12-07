class Solution:
    # Define a class named Solution. This is common in coding interview problems.

    @staticmethod
    # The @staticmethod decorator indicates that 'merge' is a static method.
    # It can be called without creating an instance of the Solution class.

    def merge(nums1, m, nums2, n):
        # Define the static method 'merge' with four parameters:
        # nums1 - first sorted list, m - number of elements in nums1 to be merged,
        # nums2 - second sorted list, n - number of elements in nums2.

        # Initialize pointers for nums1 and nums2.
        p1 = m - 1  # Pointer for the last element in nums1 that needs to be merged.
        p2 = n - 1  # Pointer for the last element in nums2.

        # Initialize a pointer for the merge position in nums1.
        p = m + n - 1  # Pointer for the last position in nums1 where the merged element will be placed.

        # Start merging from the end of both lists.
        while p1 >= 0 and p2 >= 0:
            # Continue looping until either list runs out of elements.

            if nums1[p1] > nums2[p2]:
                # If the current element in nums1 is greater than in nums2,
                # place it at the current position pointed by 'p'.
                nums1[p] = nums1[p1]
                p1 -= 1  # Move the pointer in nums1 backwards.
            else:
                # If the current element in nums2 is greater or equal to nums1,
                # place it at the current position pointed by 'p'.
                nums1[p] = nums2[p2]
                p2 -= 1  # Move the pointer in nums2 backwards.
            p -= 1  # Move the merge position pointer backwards.

        # Handle any remaining elements in nums2.
        nums1[:p2 + 1] = nums2[:p2 + 1]
        # Copy any remaining elements from nums2 to nums1. This is needed in case
        # all elements of nums1 are greater than those left in nums2.

# Example Usage
nums1 = [1, 2, 3, 0, 0, 0]  # Input array nums1 with empty spaces for merging.
m = 3  # Number of elements in nums1 to be merged.
nums2 = [2, 5, 6]  # Input array nums2.
n = 3  # Number of elements in nums2.

Solution.merge(nums1, m, nums2, n)  # Calling the static method merge.
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

