def sumInAMatrix(nums):
    """
    Calculate the score by repeatedly:
    1. From each row, select the largest number and remove it
    2. Find the highest number among all those selected
    3. Add that number to the score
    4. Repeat until the matrix is empty
    
    Args:
        nums: A 2D list of integers
    
    Returns:
        The final score
    """
    if not nums or not nums[0]:
        return 0
    
    # Sort each row in descending order
    for row in nums:
        row.sort(reverse=True)
    
    score = 0
    num_rows = len(nums)
    num_cols = len(nums[0])
    
    # Iterate through each column (which represents each round of removal)
    for col in range(num_cols):
        # Find the maximum value in this column across all rows
        max_in_col = max(nums[row][col] for row in range(num_rows))
        score += max_in_col
    
    return score

if __name__ == "__main__":
    # Test with the provided example
    nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
    result = sumInAMatrix(nums)
    print(result)  # Expected output: 15