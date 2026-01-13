class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Buy exactly two chocolates such that:
        - We minimize the sum of prices
        - We stay within our money
        - Return leftover money
        - If we can't buy two chocolates, return original money
        
        Args:
            prices: List of chocolate prices
            money: Amount of money available
        
        Returns:
            Leftover money after buying two cheapest chocolates,
            or original money if we can't afford any two
        """
        if not prices or len(prices) < 2:
            return money
        
        # Find the two cheapest chocolates
        # We can just sort and take the first two, or track two smallest values
        
        # Sort the prices
        prices.sort()
        
        # Two cheapest are prices[0] and prices[1]
        total_cost = prices[0] + prices[1]
        
        # If we can afford them, return leftover money
        if total_cost <= money:
            return money - total_cost
        else:
            # Can't afford two chocolates, return original money
            return money

if __name__ == "__main__":
    import sys
    solution = Solution()
    
    # Read prices and money from command line
    # Usage: python solution_14.py "[1,2,2]" 3
    if len(sys.argv) >= 3:
        prices_input = sys.argv[1]
        money_input = sys.argv[2]
    else:
        # Default values for testing
        prices_input = "[1,2,2]"
        money_input = "3"
    
    # Parse inputs
    prices = eval(prices_input)
    money = int(money_input)
    
    # Run the solution
    result = solution.buyChoco(prices, money)
    
    # Display the output
    print(f"\nInput:")
    print(f"  prices = {prices}")
    print(f"  money = {money}")
    print(f"\nOutput:")
    print(f"  {result}")