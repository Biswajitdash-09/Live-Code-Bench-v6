import functools

MOD = 10**9 + 7

class Solution:
    def countMethod(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        """
        Count integers x such that num1 <= x <= num2 and 
        min_sum <= digit_sum(x) <= max_sum. Return result modulo 10^9 + 7.
        """
        self.min_sum = min_sum
        self.max_sum = max_sum
        
        # Helper to decrement a string representation of a number
        def decrement(num_str):
            if num_str == "0":
                return "-1"
            num = list(num_str)
            n = len(num)
            i = n - 1
            while i >= 0 and num[i] == '0':
                num[i] = '9'
                i -= 1
            if i >= 0:
                num[i] = str(int(num[i]) - 1)
            # Remove leading zeros
            result = ''.join(num).lstrip('0')
            return result if result != "" else "0"
        
        def count(num_str):
            # Handle negative numbers (result of 0-1)
            if num_str.startswith('-'):
                return 0
            
            num = num_str
            prefix = num_str
            n = len(num)
            
            memo = {}
            
            def solve(pos, tight_idx_set, total_digits):
                if pos == n:
                    return 1 if total_digits == len(num) else 0
                
                key = (pos, tuple(sorted(tight_idx_set)), total_digits)
                if key in memo:
                    return memo[key]
                
                # Calculate max possible for remaining positions
                max_possible_remaining = len(num) - pos - 1
                
                possible_prefixes_for_this_pos = []
                for idx in tight_idx_set:
                    if idx + max_possible_remaining >= len(num):
                        possible_prefixes_for_this_pos.append(idx)
                
                # Early termination
                if len(possible_prefixes_for_this_pos) == 0:
                    memo[key] = 0
                    return 0
                
                # Get digit at trailing position
                trailing_digit = int(prefix[pos])
                
                # Determine possible digits
                if total_digits < len(num):
                    # Not leading zero anymore
                    min_digit = 1 if total_digits > 0 else 1
                    max_digit = 9
                else:
                    # Leading zero
                    min_digit = trailing_digit
                    max_digit = trailing_digit
                
                # Calculate max_possible for pruning
                current_sum = sum(int(num[i]) for i in range(pos))
                max_possible = current_sum + max_digit * (n - pos)
                min_possible = current_sum + min_digit * (n - pos)
                
                if min_possible > max_sum:
                    memo[key] = 0
                    return 0
                
                total = 0
                for i in range(min_digit, max_digit + 1):
                    if i > digit_at_prefix[i]:
                        continue
                    
                    if i < trailing_digit:
                        continue
                    
                    match_prefixes_for_digit = set()
                    for idx in possible_prefixes_for_this_pos:
                        if idx < n and idx + (n - pos - 1) >= n and digit_at_prefix[i]:
                            match_prefixes_for_digit.add(idx)
                    
                    total += solve(pos + 1, match_prefixes_for_digit, total_digits + 1)
                
                memo[key] = total % MOD
                return total
            
            # Precompute digit at each position
            digit_at_prefix = [int(num[i]) for i in range(len(num))]
            
            # Initialize with all possible tight positions
            tight_idx_set = set(range(len(num)))
            
            result = solve(0, tight_idx_set, 0)
            return result
        
        # Tabulation approach using index-based prefix matching
        def count_with_index(num_str):
            if not num_str or num_str.startswith('-'):
                return 0
            
            num = num_str
            n = len(num)
            prefix = num
            MOD = 10**9 + 7
            
            # Create digit_at_prefix for padding positions
            MAX_INDEX = 2 * n
            digit_at_prefix = [0] * MAX_INDEX
            for i in range(n):
                if i < len(prefix):
                    digit_at_prefix[i] = ord(prefix[i]) - ord('0')
            
            @functools.lru_cache(maxsize=None)
            def solve(pos, tight_idx_count, leading_zero):
                if pos == n:
                    return 1  # Valid configuration
                
                # Calculate tight index set from count (inverse mapping)
                max_possible_remaining = n - pos - 1
                
                # Reconstruct tight indices
                tight_indices = set()
                for idx in range(MAX_INDEX):
                    if idx < n and max_possible_remaining == 0:
                        tight_indices.add(idx)
                    elif idx + max_possible_remaining >= MAX_INDEX:
                        tight_indices.add(idx)
                
                if not tight_indices:
                    return 0
                
                # Pre-compute max_possible for pruning
                max_possible = tight_idx_count * 9 + max_possible_remaining * 9
                min_possible = 0
                
                if min_possible > max_sum:
                    return 0
                
                # Range of permitted digits
                permitted_high = 9
                permitted_low = 1 if not leading_zero else 0
                
                # Find min and max digit_at_prefix among all tight indices
                min_prefix_digit = 0
                max_prefix_digit = 9
                if tight_idx_count > 0:
                    for idx in range(max(0, pos - max_idx + 1), min(59, pos + 2)):
                        if idx >= 0 and idx < MAX_INDEX:
                            d = digit_at_prefix[min(idx, len(prefix) - 1)]
                            min_prefix_digit = max(min_prefix_digit, d)
                            max_prefix_digit = min(max_prefix_digit, d)
                
                permitted_low = max(permitted_low, min_prefix_digit)
                permitted_high = min(permitted_high, max_prefix_digit)
                
                if permitted_low > permitted_high:
                    return 0
                
                # Check prefixes for this digit_range
                match_prefixes_for_digit = set()
                for j in range(permitted_low, permitted_high + 1):
                    for i in range(max(0, pos - j), min(59, pos + j + 1)):
                        if i >= 0 and i < MAX_INDEX and digit_at_prefix[i] == j:
                            match_prefixes_for_digit.add(i)
                
                new_tight_idx_count = 0
                max_idx = 0
                for idx in match_prefixes_for_digit:
                    if idx > max_idx:
                        max_idx = idx
                new_tight_idx_count = max_idx + 1
                
                total = 0
                for digit in range(permitted_low, permitted_high + 1):
                    total += solve(pos + 1, new_tight_idx_count, False)
                
                return total % MOD
            
            return solve(0, len(num), True)
        
        # Optimized digit DP solution
        def count_optimized(num_str):
            if not num_str or num_str.startswith('-'):
                return 0
            
            num = num_str
            n = len(num)
            
            @functools.lru_cache(maxsize=None)
            def dfs(pos, sum_so_far, tight):
                if pos == len(num):
                    return 1 if self.min_sum <= sum_so_far <= self.max_sum else 0
                
                limit = int(num[pos]) if tight else 9
                total = 0
                
                for digit in range(limit + 1):
                    new_sum = sum_so_far + digit
                    if new_sum > self.max_sum:
                        continue  # Prune impossible branches
                    
                    new_tight = tight and (digit == limit)
                    total += dfs(pos + 1, new_sum, new_tight)
                
                return total % MOD
            
            return dfs(0, 0, True)
        
        # Calculate result = count(num2) - count(num1-1)
        result = (count_optimized(num2) - count_optimized(decrement(num1))) % MOD
        return result