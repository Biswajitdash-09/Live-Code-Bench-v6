def countSeniors(details):
    """
    Count passengers who are strictly more than 60 years old.
    
    Each passenger detail string has format:
    - Characters 0-9: phone number (10 chars)
    - Character 10: gender (M/F/O)
    - Characters 11-12: age (2 chars)
    - Characters 13-14: seat number (2 chars)
    
    Args:
        details: List of 15-character strings with passenger info
    
    Returns:
        Count of passengers older than 60
    """
    count = 0
    for passenger in details:
        # Age is at positions 11 and 12 (0-indexed)
        age = int(passenger[11:13])
        if age > 60:
            count += 1
    return count

if __name__ == "__main__":
    # Test with the provided example
    details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    result = countSeniors(details)
    print(result)  # Expected output: 2