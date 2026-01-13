def maximum_or(nums, k):
    """
    Maximum OR problem: Maximize the bitwise OR of array elements by doubling at most k times.
    
    Args:
        nums: List of integers
        k: Maximum number of doubling operations
    
    Returns:
        Maximum possible OR value
    """
    n = len(nums)
    current_or = 0
    
    # Calculate current OR with all elements
    for num in nums:
        current_or |= num
    
    max_result = current_or
    
    # Greedy approach: find indices that contribute most when doubled
    # Track how many times each index has been doubled
    doubled_times = [0] * n
    
    # Use k operations greedily
    for _ in range(k):
        best_index = -1
        best_value = 0
        
        for i in range(n):
            # Try doubling each element and see what OR we get
            temp = 1 << doubled_times[i]
            nums[i] *= 2
            doubled_times[i] += 1
            
            # Calculate new OR
            new_or = 0
            for j in range(n):
                new_or |= nums[j]
            
            # Check if this gives improvement
            improvement = new_or - current_or
            
            if improvement > best_value:
                best_value = improvement
                best_index = i
            
            # Revert the change
            doubled_times[i] -= 1
            nums[i] //= 2
        
        if best_index != -1:
            # Apply the best doubling
            doubled_times[best_index] += 1
            nums[best_index] *= 2
            current_or = current_or | nums[best_index]
            max_result = max(max_result, current_or)
    
    return max_result


def maximum_or_optimized(nums, k):
    """
    Optimized approach using backtracking with depth limit.
    """
    n = len(nums)
    
    if n == 0:
        return 0
    
    def backtrack(nums, operations_left):
        """
        Backtrack to find maximum OR by exploring doubling options.
        Returns the maximum OR value achievable.
        """
        # Calculate current OR of the array
        current_or = 0
        for num in nums:
            current_or |= num
        
        if operations_left == 0:
            return current_or
        
        max_result = current_or
        
        for i in range(len(nums)):
            # Try doubling this element
            num_before = nums[i]
            nums[i] *= 2
            
            # Recurse to explore further doublings
            result = backtrack(nums, operations_left - 1)
            max_result = max(max_result, result)
            
            # Restore original value for backtracking
            nums[i] = num_before
        
        return max_result
    
    # For efficiency, we only do full backtracking if k is small
    if k <= 10:
        return backtrack(nums.copy(), k)
    else:
        # Fall back to greedy for larger k
        return maximum_or(nums.copy(), k)


# Test the solution
if __name__ == "__main__":
    # Example from problem
    nums = [12, 9]
    k = 1
    result = maximum_or_optimized(nums, k)
    print(f"nums = {nums}, k = {k}")
    print(f"Maximum OR: {result}")
    print(f"  Verification: 12 = 01100, 18 = 10010, OR = 11110 = 30")
    
    # Additional test cases
    print("\nTest cases:")
    
    # Test 1: Simple case
    nums1 = [1, 2, 4]
    k1 = 2
    result1 = maximum_or_optimized(nums1.copy(), k1)
    print(f"nums = {nums1}, k = {k1} -> {result1}")
    print(f"  Verification: 1 | 2 | 16 = 10011 = 19")
    
    # Test 2: All same numbers
    nums2 = [3, 3, 3]
    k2 = 3
    result2 = maximum_or_optimized(nums2.copy(), k2)
    print(f"nums = {nums2}, k = {k2} -> {result2}")
    print(f"  Verification: 3 | 3 | 24 = 11011 = 27")
    
    # Test 3: Single element
    nums3 = [5]
    k3 = 3
    result3 = maximum_or_optimized(nums3.copy(), k3)
    print(f"nums = {nums3}, k = {k3} -> {result3}")
    print(f"  Verification: 5 * 2^3 = 40")
    
    # Test 4: Large k
    nums4 = [1, 1, 1]
    k4 = 5
    result4 = maximum_or_optimized(nums4.copy(), k4)
    print(f"nums = {nums4}, k = {k4} -> {result4}")
    print(f"  Verification: 1 | 1 | 32 = 100001 = 33")