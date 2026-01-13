def doesValidArrayExist(derived):
    """
    Determine if there exists a valid binary array original that could have formed derived.
    
    The derived array is computed as:
    - For i in [0, n-2]: derived[i] = original[i] XOR original[i+1]
    - For i = n-1: derived[n-1] = original[n-1] XOR original[0]
    
    Args:
        derived: List of integers representing the derived array
        
    Returns:
        bool: True if a valid original array exists, False otherwise
    """
    n = len(derived)
    
    # Try with original[0] = 0
    original = [0] * n
    for i in range(n - 1):
        original[i + 1] = original[i] ^ derived[i]
    
    # Check if the last condition holds
    if derived[n - 1] == original[n - 1] ^ original[0]:
        return True
    
    # Try with original[0] = 1
    original = [1] * n
    for i in range(n - 1):
        original[i + 1] = original[i] ^ derived[i]
    
    # Check if the last condition holds
    if derived[n - 1] == original[n - 1] ^ original[0]:
        return True
    
    return False


# Simpler optimization: we only need to check if the XOR of all derived values is 0
# This is because:
# original[0] ^ original[1] = derived[0]
# original[1] ^ original[2] = derived[1]
# ...
# original[n-1] ^ original[0] = derived[n-1]
#
# XORing all equations together:
# original[0] appears twice and cancels out
# original[1] appears twice and cancels out
# ...
# So we're left with: 0 = derived[0] ^ derived[1] ^ ... ^ derived[n-1]
#
# Therefore, a valid original array exists iff the XOR of all derived values is 0

def doesValidArrayExistOptimized(derived):
    """
    Optimized version: a valid original array exists iff XOR of all derived values is 0.
    
    Args:
        derived: List of integers representing the derived array
        
    Returns:
        bool: True if a valid original array exists, False otherwise
    """
    xor_sum = 0
    for val in derived:
        xor_sum ^= val
    return xor_sum == 0


# Main function using the optimized approach
def doesValidArrayExistMain(derived):
    return doesValidArrayExistOptimized(derived)