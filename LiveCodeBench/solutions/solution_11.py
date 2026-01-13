class Solution:
    def maximumOr(self, nums, k):
        """
        Maximize the bitwise OR of all elements after at most k multiplications by 2.
        
        Args:
            nums: List of integers
            k: Maximum number of multiplications by 2 allowed
        
        Returns:
            Maximum possible value of bitwise OR
        """
        # Greedy approach: try each possible multiplication to see which gives best improvement
        for _ in range(k):
            best_index = -1
            best_or = 0
            
            # Try doubling each element and see which gives the best OR
            for i in range(len(nums)):
                nums[i] *= 2
                current_or = 0
                for num in nums:
                    current_or |= num
                if current_or > best_or:
                    best_or = current_or
                    best_index = i
                nums[i] //= 2  # Undo the multiplication
            
            # Apply the best multiplication
            if best_index != -1:
                nums[best_index] *= 2
        
        # Calculate final OR
        result = 0
        for num in nums:
            result |= num
        return result

def maximum_or(nums, k):
    """
    Wrapper function for backward compatibility
    """
    solution = Solution()
    return solution.maximumOr(nums.copy(), k)

if __name__ == "__main__":
    # Test with Example 1
    solution = Solution()
    nums1 = [12, 9]
    k1 = 1
    result1 = solution.maximumOr(nums1.copy(), k1)
    print(f"Example 1: {result1} (expected: 30)")
    
    # Test with Example 2
    nums2 = [8, 1, 2]
    k2 = 2
    result2 = solution.maximumOr(nums2.copy(), k2)
    print(f"Example 2: {result2}")