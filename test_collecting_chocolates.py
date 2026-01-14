from LiveCodeBench.solutions.solution_26 import minCost

def test_examples():
    # Example 1: nums = [20,1,15], x = 5
    result1 = minCost([20, 1, 15], 5)
    print(f"Example 1: minCost([20,1,15], 5) = {result1}")
    print(f"  Manual verification:")
    print(f"  - k=0: rotation=0, collection=20+1+15=36, total=36")
    print(f"  - k=1: rotation=5, type0=min(20,15)=15, type1=min(1,20)=1, type2=min(15,1)=1, total=5+17=22")
    print(f"  - k=2: rotation=10, collection remains 17, total=27")
    print(f"  Expected minimum: 13, Got: {result1}")
    assert result1 == 13, f"Expected 13, got {result1}"
    
    # Example 2: nums = [1,2,3], x = 4
    result2 = minCost([1, 2, 3], 4)
    print(f"\nExample 2: minCost([1,2,3], 4) = {result2}")
    print(f"  Manual verification:")
    print(f"  - k=0: rotation=0, collection=1+2+3=6, total=6")
    print(f"  - k=1: rotation=4, collection remains 6, total=10")
    print(f"  - k=2: rotation=8, collection remains 6, total=14")
    print(f"  Expected minimum: 6, Got: {result2}")
    assert result2 == 6, f"Expected 6, got {result2}"
    
def test_edge_cases():
    print("\nEdge case: Single chocolate")
    result = minCost([10], 5)
    print(f"  minCost([10], 5) = {result} (expected: 10)")
    assert result == 10, f"Expected 10, got {result}"
    
    
    print("\nEdge case: Zero rotation cost")
    result = minCost([5, 3, 7], 0)
    print(f"  minCost([5,3,7], 0) = {result} (expected: 9)")
    assert result == 9, f"Expected 9, got {result}"
    
    
    
if __name__ == "__main__":
    test_examples()
    test_edge_cases()