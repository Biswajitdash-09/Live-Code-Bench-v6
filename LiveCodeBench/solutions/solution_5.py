import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Vanya can always win within 3 turns:
        # If n % 3 == 0: After Vanya's first move, the number is n±1 ≡ ±1 (mod 3)
        #                Then Vova moves to one of the two adjacent values
        #                On Vanya's second move (move 3), he can reach a multiple of 3
        # If n % 3 == 1: Vanya subtracts 1 to reach a multiple of 3 on move 1
        # If n % 3 == 2: Vanya adds 1 to reach a multiple of 3 on move 1
        results.append("First")
    
    print('\n'.join(results))

if __name__ == "__main__":
    solve()