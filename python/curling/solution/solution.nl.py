import math

def inch2meter(inch):
    
    return inch * 0.0254

def binnenhuis(x, y, inch=True):
    
    """
    >>> binnenhuis(70.0, 0.0)
    True
    >>> binnenhuis(70.0, 0.0, inch=False)
    False
    >>> binnenhuis(78.0, 0.0)
    False
    """

    # straal van huis bepalen (in inch)
    straalHuis = 6 * 12
    straalSteen = 36 / (2 * math.pi)
    
    # stralen omzetten naar meter (indien nodig)
    if not inch:
        straalHuis = inch2meter(straalHuis)
        straalSteen = inch2meter(straalSteen)
        
    # afstand tot middelpunt bepalen
    afstand = (x ** 2 + y ** 2) ** 0.5
    
    # bepaal of steen (gedeeltelijk) in het huis ligt
    return afstand <= straalHuis + straalSteen

def geldigePosities(stenen, inch=True):
    
    """
    >>> geldigePosities([(20.0, 10.0, 'R'), (25.0, 22.0, 'G'), (42.0, 37.0, 'R')])
    True
    >>> geldigePosities([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'G')])
    True
    >>> geldigePosities([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
    True
    """
    
    # controleren of er meer dan acht rode stenen zijn
    if len([steen for steen in stenen if steen[2] == 'R']) > 8:
        return False

    # controleren of er meer dan acht gele stenen zijn
    if len([steen for steen in stenen if steen[2] == 'G']) > 8:
        return False
    
    # straal van stenen bepalen (in inch of in meter)
    straalSteen = 36 / (2 * math.pi)
    if not inch:
        straalSteen = inch2meter(straalSteen)
        
    # controleren of er stenen overlappen
    for index1, steen1 in enumerate(stenen[:-1]):
        x1, y1 = steen1[:2]
        for steen2 in stenen[index1 + 1:]:
            x2, y2 = steen2[:2]
            if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < 2 * straalSteen:
                return False
            
    # alle voorwaarden zijn voldaan
    return True

def score(stenen, inch=True):
    
    """
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'G'), (42.0, 37.0, 'R')])
    (1, 0)
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'G')])
    (2, 0)
    >>> score([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')])
    (3, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'G'), (1.0668, 0.9398, 'R')], False)
    (1, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'G')], inch=False)
    (2, 0)
    >>> score([(0.508, 0.254, 'R'), (0.635, 0.5588, 'R'), (1.0668, 0.9398, 'R')], False)
    (3, 0)
    """
    
    # nagaan of de posities van de stenen geldig zijn
    assert geldigePosities(stenen, inch), 'ongeldige posities van stenen'
    
    # stenen rangschikken volgens stijgende afstand tot middelpunt
    stenen = sorted(
        (steen for steen in stenen if binnenhuis(*steen[:2], inch)), 
        key=lambda p: p[0] ** 2 + p[1] ** 2
    )
    
    # kleur van dichtste steen bepalen
    # OPMERKING: waarde None toegekend als er geen stenen in het huis liggen
    kleur = stenen[0][2] if stenen else None

    # bepaal score
    score = 0
    while score < len(stenen) and stenen[score][2] == kleur:
        score += 1
    
    # score teruggeven als een tuple (rood, geel)
    return (score, 0) if kleur == 'R' else (0, score)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
