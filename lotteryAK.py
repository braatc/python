'''
matches(ticket, winners) reports how well a lottery ticket did
test_matches(matches) reports whether a matches() function works as assigned.
'''

def matches(ticket, winner):
    ''' returns the number of numbers that are in both ticket and winner
    
    ticket and winner are each a list of five unique ints
    
    returns an int from 0 to 5 inclusive.
    '''
    # Could be done more effectively using the Python "set" type,
    # but that is not standard across programming languages
    # and is not introduced in the course. Could be:
    # return len(set(ticket) & set(winners))
    score = 0
    for number in ticket:
        if number in winner:
            score += 1
    return score
            
