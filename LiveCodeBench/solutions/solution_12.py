class Solution:
    def maxStrength(self, nums):
        """
        Find the maximum product of a non-empty subset of the array.
        
        The strategy is:
        1. Sort the array to easily identify which negative numbers to exclude
        2. If we have an odd number of negative numbers, exclude the one with the
           smallest absolute value (i.e., the largest negative number, closest to zero)
        3. Handle edge cases like all zeros or single negative number
        
        Args:
            nums: List of integers
        
        Returns:
            Maximum possible product of a non-empty subset
        """
        n = len(nums)
        
        # If there's only one element, return it
        if n == 1:
            return nums[0]
        
        # Sort the array
        nums.sort()
        
        # Count negative numbers
        neg_count = sum(1 for num in nums if num < 0)
        
        # If there's an odd number of negative numbers, we need to exclude one
        # We exclude the one with the smallest absolute value (largest negative)
        exclude_index = -1
        if neg_count % 2 == 1:
            # Find the negative number closest to zero (with smallest absolute value)
            # Since array is sorted, this is the last negative number
            for i in range(n - 1, -1, -1):
                if nums[i] < 0:
                    exclude_index = i
                    break
        
        # Calculate the product excluding the identified negative number
        product = 1
        has_non_zero = False
        
        for i in range(n):
            # Skip the excluded negative number
            if i == exclude_index:
                continue
            # Skip zeros - they don't affect the product in a positive way
            if nums[i] == 0:
                continue
            product *= nums[i]
            has_non_zero = True
        
        # If we couldn't include any non-zero numbers (e.g., all zeros or one negative excluded)
        # We need to return the maximum single element
        if not has_non_zero:
            # If all are zeros except one negative which we excluded
            if exclude_index != -1 and all(num == 0 for num in nums if exclude_index != nums.index(num) if num != nums[exclude_index]):
                # Return the negative number (we had to exclude it but it's the only non-zero)
                return nums[exclude_index]
            # Return 0 if everything else is 0
            return 0
        
        return product

if __name__ == "__main__":
    solution = Solution()
    
    # Test with provided example
    nums1 = [3,-1,-5,2,5,-9]
    result1 = solution.maxStrength(nums1)
    print(f"Test 1: nums = {nums1}")
    print(f"Result: {result1}")
    print(f"Expected: 1350 (3 * -1 * -5 * 2 * 5 * -9 excluding -1 or similar)")
    print()
    
    # Test with all positives
    nums2 = [1, 2, 3]
    result2 = solution.maxStrength(nums2)
    print(f"Test 2: nums = {nums2}")
    print(f"Result: {result2}")
    print(f"Expected: 6")
    print()
    
    # Test with all negatives (even count)
    nums3 = [-1, -2, -3, -4]
    result3 = solution.maxStrength(nums3)
    print(f"Test 3: nums = {nums3}")
    print(f"Result: {result3}")
    print(f"Expected: 24")
    print()
    
    # Test with single negative
    nums4 = [-1]
    result4 = solution.maxStrength(nums4)
    print(f"Test 4: nums = {nums4}")
    print(f"Result: {result4}")
    print(f"Expected: -1")
    print()
    
    # Test with single positive
    nums5 = [1]
    result5 = solution.maxStrength(nums5)
    print(f"Test 5: nums = {nums5}")
    print(f"Result: {result5}")
    print(f"Expected: 1")
    print()
    
    # Test with zeros and negatives
    nums6 = [0, -1]
    result6 = solution.maxStrength(nums6)
    print(f"Test 6: nums = {nums6}")
    print(f"Result: {result6}")
    print(f"Expected: 0 (or -1 if we can choose -1)")
    print()
    
    # Test with mixed
    nums7 = [3, -2, 1, 4]
    result7 = solution.maxStrength(nums7)
    print(f"Test 7: nums = {nums7}")
    print(f"Result: {result7}")
    print(f"Expected: 24 (3 * -2 * 1 * 4)")