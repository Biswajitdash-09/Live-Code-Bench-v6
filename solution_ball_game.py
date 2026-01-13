import sys
from typing import List

def find_losers(n: int, k: int) -> List[int]:
    """
    Find the losers of the ball passing game.
    Friends are numbered 1 to n, sitting in a circle.
    Ball starts with friend 1, then passes i*k steps each turn.
    Game ends when a friend receives the ball twice.
    """
    if n <= 0:
        return []
    
    if k == 0:
        # Ball stays with friend 1 forever
        return list(range(2, n + 1))
    
    visited = set()
    current = 0  # Friend 1 has index 0
    
    while True:
        if current in visited:
            break
        
        visited.add(current)
        turn = len(visited)  # Which pass this is (1st, 2nd, 3rd, etc.)
        steps = turn * k
        current = (current + steps) % n
    
    # Losers are friends who never received the ball
    losers = [i + 1 for i in range(n) if i not in visited]
    return losers

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    outputs = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        k = int(data[idx])
        idx += 1
        
        result = find_losers(n, k)
        outputs.append(' '.join(map(str, result)))
    
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()