def maximumNumberOfStringPairs(words):
    seen = set()
    count = 0
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in seen:
            count += 1
            seen.remove(reversed_word)
        else:
            seen.add(word)
    return count