def almostIncreasingSequence(sequence):
    previous = -999999999
    counter = 0
    for item in sequence:
        if previous >= item:
            counter = counter + 1
        if counter > 1:
            return False
        previous = item
    return True
