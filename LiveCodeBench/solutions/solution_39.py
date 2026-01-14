def relocateMarbles(nums, moveFrom, moveTo):
    occupied = set(nums)
    
    for from_pos, to_pos in zip(moveFrom, moveTo):
        if from_pos in occupied:
            occupied.remove(from_pos)
        occupied.add(to_pos)
    
    return sorted(occupied)