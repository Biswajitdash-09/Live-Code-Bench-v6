class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        """
        Calculate the distinct difference array where:
        diff[i] = (number of distinct elements in nums[0...i]) - 
                  (number of distinct elements in nums[i+1...n-1])
        
        Args:
            nums: Input list of integers
            
        Returns:
            The distinct difference array
        """
        n = len(nums)
        diff = [0] * n
        
        # Precompute prefix distinct counts
        prefix_distinct = [0] * n
        seen = set()
        for i in range(n):
            seen.add(nums[i])
            prefix_distinct[i] = len(seen)
        
        # Precompute suffix distinct counts
        suffix_distinct = [0] * n
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(nums[i])
            suffix_distinct[i] = len(seen)
        
        # Calculate diff array
        for i in range(n):
            if i < n - 1:
                # Suffix part is from i+1 to n-1
                suffix_count = suffix_distinct[i + 1]
            else:
                # Suffix is empty
                suffix_count = 0
            
            diff[i] = prefix_distinct[i] - suffix_count
        
        return diff

if __name__ == "__main__":
    import sys
    solution = Solution()
    
    # Read nums from command line
    # Usage: python solution_16.py "[1,2,3,4,5]"
    if len(sys.argv) >= 2:
        nums_input = sys.argv[1]
    else:
        # Default values for testing
        nums_input = "[1,2,3,4,5]"
    
    # Parse input
    nums = eval(nums_input)
    
    # Run the solution
    result = solution.distinctDifferenceArray(nums)
    
    # Display the output
    print(f"\nInput:")
    print(f"  nums = {nums}")
    print(f"\nOutput:")
    print(f"  {result}")