class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        """
        Calculate the minimum cost to collect chocolates of all types.
        
        We can perform k rotations (0 <= k < n).
        For a fixed k, we pay k * x for operations.
        For each chocolate type i, we can buy it at the cheapest price
        among all rotations 0 to k.
        
        Type i is at index (i - r) % n after r rotations.
        """
        n = len(nums)
        
        # Initialize min_costs with the 0-th rotation (original costs)
        # min_costs[i] stores the minimum cost to buy chocolate of type i
        # considering rotations 0 to k
        min_costs = list(nums)
        
        # Initial answer with 0 rotations
        ans = sum(min_costs)
        
        # Try rotations from 1 to n-1
        for k in range(1, n):
            # For each type i, check if the cost at current rotation k is cheaper
            # The cost of type i at rotation k is nums[(i - k) % n]
            current_sum = 0
            for i in range(n):
                min_costs[i] = min(min_costs[i], nums[(i - k) % n])
                current_sum += min_costs[i]
            
            # Total cost = cost of operations + sum of cheapest prices
            total_cost = k * x + current_sum
            ans = min(ans, total_cost)
            
        return ans