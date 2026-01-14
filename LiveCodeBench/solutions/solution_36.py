from math import gcd
from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        """
        Count beautiful pairs where the first digit of nums[i] and the last digit 
        of nums[j] are coprime (gcd == 1), for all i < j.
        
        Args:
            nums: List of integers
            
        Returns:
            Number of beautiful pairs
        """
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Get first digit of nums[i]
            first_digit = int(str(nums[i])[0])
            
            for j in range(i + 1, n):
                # Get last digit of nums[j]
                last_digit = nums[j] % 10
                
                # Check if first digit and last digit are coprime
                if gcd(first_digit, last_digit) == 1:
                    count += 1
        
        return count