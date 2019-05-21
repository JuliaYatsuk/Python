def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    first = racers.pop(0)
    last = racers.pop(-1)
    racers.append(first)
    racers.insert(0, last)
    return racers
        

print( purple_shell([1,2,3]))
