from collections import Counter

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """
        Minimize string length by repeatedly removing pairs of same characters.
        
        Operation: Choose an index i where character c appears, then:
        - Delete the closest occurrence of c to the left of index i (if any)
        - Delete the closest occurrence of c to the right of index i (if any)
        
        The answer is the number of unique characters in the string,
        because each unique character can have at most one occurrence remain
        after all possible operations are performed.
        """
        return len(Counter(s))