import math

def inch2meter(inch):
    
    return inch * 0.0254

def inHouse(x, y, inch=True):
    
    """
    >>> inHouse(70.0, 0.0)
    True
    >>> inHouse(70.0, 0.0, inch=False)
    False
    >>> inHouse(78.0, 0.0)
    False
    """

    # determine radius of the house (in inch)
    radiusHouse = 6 * 12
    radiusStone = 36 / (2 * math.pi)
    
    # convert radiuses into meter (if necessary)
    if not inch:
        radiusHouse = inch2meter(radiusHouse)
        radiusStone = inch2meter(radiusStone)
      
    # determine distance to center  
    distance = (x ** 2 + y ** 2) ** 0.5
    
    # determine if stone overlaps with the house
    return distance <= radiusHouse + radiusStone

def validPositions(stones, inch=True):
    
    """
    >>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')])
    True
    >>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')])
    True
    >>> validPositions([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
    True
    """
    
    # check if there are not more than eight red stones
    if len([stone for stone in stones if stone[2] == 'R']) > 8:
        return False

    # check if there are not more than eight yellow stones
    if len([stone for stone in stones if stone[2] == 'Y']) > 8:
        return False
    
    # determine radius of stones (in inch or in meter)
    radiusStone = 36 / (2 * math.pi)
    if not inch:
        radiusStone = inch2meter(radiusStone)

    # check if there are overlapping stones        
    for index1, stone1 in enumerate(stones[:-1]):
        x1, y1 = stone1[:2]
        for stone2 in stones[index1 + 1:]:
            x2, y2 = stone2[:2]
            if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < 2 * radiusStone:
                return False
            
    # all conditions are fulfilled
    return True

def score(stones, inch=True):
    
    """
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')])
    (1, 0)
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')])
    (2, 0)
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
    (3, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'Y'), (1.0668, 0.9398, 'R')], False)
    (1, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'Y')], inch=False)
    (2, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'R')], False)
    (3, 0)
    """
    
    # check if positions of stones is valid
    assert validPositions(stones, inch), 'invalid stone positions'
    
    # arrange stones in increasing distance to the center
    stones = sorted(
        (stone for stone in stones if inHouse(*stone[:2], inch)), 
        key=lambda p: p[0] ** 2 + p[1] ** 2
    )
    
    # determine color of stone that is closest to the center
    # NOTE: value None is assigned if there are no stones in the house
    color = stones[0][2] if stones else None

    # calculate score
    score = 0
    while score < len(stones) and stones[score][2] == color:
        score += 1
    
    # return scores as a tuple (red, yellow)
    return (score, 0) if color == 'R' else (0, score)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()