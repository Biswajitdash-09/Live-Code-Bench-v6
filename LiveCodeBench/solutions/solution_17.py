class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Track number of adjacent pairs with same non-zero color after each query.
        
        Args:
            n: size of the array
            queries: list of [index, color] operations
            
        Returns:
            list of counts after each query
        """
        nums = [0] * n
        result = []
        
        # Helper to check if two indices form a matching pair
        def is_pair(i, j):
            return nums[i] != 0 and nums[i] == nums[j]
        
        for index, color in queries:
            old_color = nums[index]
            
            # Remove old matches if they existed
            change = 0
            if index > 0 and index < n and is_pair(index - 1, index):
                change -= 1
            if index >= 0 and index < n - 1 and is_pair(index, index + 1):
                change -= 1
            
            # Update the color
            nums[index] = color
            
            # Add new matches if they exist
            if index > 0 and index < n and is_pair(index - 1, index):
                change += 1
            if index >= 0 and index < n - 1 and is_pair(index, index + 1):
                change += 1
            
            # Store the count after this query
            # We track the count incrementally
            if not result:
                result.append(change)
            else:
                result.append(result[-1] + change)
        
        return result