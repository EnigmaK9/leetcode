class Solution:
    def removeDuplicates(self, nums):
        # If the length of the list is less than 2, no duplicates can exist
        if len(nums) < 2:
            return len(nums)

        # Initialize two pointers, both starting at index 2
        slow, fast = 2, 2

        # Iterate through the array with the fast pointer
        while fast < len(nums):
            # If the current number is not equal to the number 2 positions before the slow pointer
            if nums[slow - 2] != nums[fast]:
                # Move the slow pointer and update the number at the slow pointer
                nums[slow] = nums[fast]
                slow += 1
            # Always move the fast pointer
            fast += 1

        # The slow pointer index is also the new length of the array without duplicates
        return slow

# Example usage
sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))  # Output: 5 ([1, 1, 2, 2, 3])

