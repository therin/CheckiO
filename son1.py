def straight(ranks):    
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5            

def flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

print test()