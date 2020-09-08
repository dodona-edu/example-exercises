from itertools import chain
import os
import imp
import sys
import random
join = os.path.join
random.seed(141414)

solution = imp.load_source( 'solution', os.path.join('..', 'solution', 'solution.en.py'))

fs = [solution.inHouse, solution.score]


drawcurl = '<DEFINITION>\n{}\n</DEFINITION>'.format(open('draw_curl.py', 'r').read())

settings = '''
-------------------------------------------------
tab name: {tabname}
{add}<LANGUAGE code="nl">
    <function from="{name1}" to="binnenhuis" />
    <function from="{name3}" to="geldigePosities" />
    <token from="Y" to="G" />
    <fixed from="invalid stone positions" to="ongeldige posities van stenen" />
</LANGUAGE>
'''.strip().format(name1=fs[0].__name__, name2=fs[1].__name__, tabname='{tabname}', add='{add}', name3=solution.validPositions.__name__)


from math import cos, sin, pi
def rotate(r, phi):
    return tuple(round(x, 1) for x in (cos(phi)*r, -sin(phi)*r))

inchborder = 6*12 + 36/(2*pi)

num = 0
f = fs[num]
print(settings.format(tabname=f.__name__, add='').strip(), file=open(join('..', 'evaluation', '{}.out'.format(num)), 'w'))
with open(join('..', 'evaluation', '{}.in'.format(num)), 'w') as inFile:
    
    staticcases = [
(70.0, 0.0, None),
(70.0, 0.0, False),
(78.0, 0.0, None),
(0.0, 0.0, None),
]
    cases = staticcases
    def gendist():
        dist = random.normalvariate(inchborder, 13)
        if abs(inchborder - dist)/abs(inchborder) < 1e-04:
            return gendist()
        else:
            return dist
    
    newcases = []
    tests = 30
    for i in range(tests):
        phi = (i * 2*pi)/tests
        dist = gendist()
        x, y = rotate(dist, phi)
        newcases.append((x, y, True if random.random() > 0.66 else None))

    tests = 30
    for i in range(tests):
        phi = (i * 2*pi)/tests
        dist = 0.0254 * gendist()
        x, y = rotate(dist, phi)
        newcases.append((x, y, False))
    
    tests = 40
    for i in range(tests):
        dist = ((i * 90)/tests) * [1, 0.0254][i%2]
        phi = (i * 2*pi)/tests
        x, y = rotate(dist, phi)
        newcases.append((x, y, [None, False][i%2]))

    #random.shuffle(newcases)
    placedrawer = True
    cases += newcases
    for x, y, inch in cases:
        if inch is None:
            print('>>> {}({!r}, {!r})'.format(f.__name__, x, y), file=inFile)
        else:
            print('>>> {}({!r}, {!r}, inch={!r})'.format(f.__name__, x, y, inch), file=inFile)

        if placedrawer:
            placedrawer = False
            print(drawcurl, file=inFile)

        try:
            if inch is None:
                result = f(x, y)
            else:
                result = f(x, y, inch=inch)
            print('''
<OUTPUTPROCESSOR>
DrawCurl([({!r}, {!r}, {!r}),], {!r})
</OUTPUTPROCESSOR>'''.format(x, y, 'Y', inch).strip(), file=inFile)

            print(repr(result), file=inFile, end='\n\n')
        except AssertionError as ae:
            print('Traceback (most recent call last):', file=inFile)
            print('AssertionError: {}'.format(str(ae)), file=inFile, end='\n\n')


num = 2
f = fs[1]
print(settings.format(tabname=f.__name__, add='').strip(), file=open(join('..', 'evaluation', '{}.out'.format(num)), 'w'))
with open(join('..', 'evaluation', '{}.in'.format(num)), 'w') as inFile:
    staticcases = [
([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')], None),
([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')], None),
([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')], None),
([(-40.2, -18.7, 'Y'), (-51.6, -26.5, 'Y'), (-56.3, 49.6, 'Y'), (-12.6, 59.9, 'R'), (11.6, -11.7, 'R'), (26.4, 39.3, 'R'), (37.3, 5.5, 'R'), (46.6, 37.0, 'R'), (8.6, -68.6, 'Y'), (47.7, 4.4, 'Y'), (24.3, 35.5, 'Y')], None),
([(1.11, -1.28, 'Y'), (-1.04, -1.28, 'R'), (-0.0, -0.88, 'Y'), (-1.04, -1.03, 'R'), (-1.05, -0.83, 'R'), (-0.39, 0.7, 'Y'), (0.18, -0.56, 'Y'), (-0.07, -0.02, 'R'), (0.2, -0.63, 'R')], False),
([(31.3, 47.2, 'R'), (-26.3, 31.3, 'R'), (-28.7, -29.5, 'R'), (10.0, -18.4, 'R'), (-17.6, -0.3, 'Y'), (-6.0, -12.2, 'R'), (14.0, 3.8, 'R'), (17.9, -8.4, 'R'), (-15.0, 25.1, 'R'), (-20.2, 23.1, 'Y'), (4.4, 59.5, 'Y')], None),
([(20.0, 10.0, 'R'), (-60.9, -64.9, 'Y') ,(25.0, 22.0, 'R'), (79.0, -0.0, 'R'), (-83.0, -0.0, 'Y')], None),

]
    cases = staticcases

    #FIXME, TODO, how many stones?

    def genPoint(low=0, high=100):
        dist = (high - low) * random.random() + low
        phi = 2 * pi * random.random()
        x, y = rotate(dist, phi)
        return x, y

    othercases = []
    
    othercases.append(([rotate(79, (i/8) * 2*pi) + (random.choice(('R', 'Y')),) for i in range(8)], None))   
    
    random.seed(1414141414)
    while len(othercases) + len(cases) < 60:
        meter = random.random() > 0.5
        #factor = 0.0254 if meter else 1
        factor = 1

        nrItems = random.randint(5, 10)
        if random.random() < 0.86:
            colors = (['R'] * (nrItems//2)) + (['Y'] * (nrItems - (nrItems//2)))
        else:
            colors = [random.choice(('R', 'Y')),] * nrItems

        random.shuffle(colors)

        items = [genPoint(0, factor*100) + (color,) for color in colors]

        if max(sum(color == k for _, _, color in items) for k in 'RY') <= 8:
        #make sure no stones overlap
            if all(all(  (((x0 - x1)**2  + (y0 - y1)**2)**0.5/factor) > 12 for i1, (x1, y1, _) in enumerate(items)  if i0 != i1   )   for i0, (x0, y0, _) in enumerate(items)):
                if all(all(  ( abs(( x0**2 + y0**2) - (x1**2 + y1**2)) > 2  )  for i1, (x1, y1, _) in enumerate(items)  if i0 != i1   )   for i0, (x0, y0, _) in enumerate(items)):
                    if meter:
                        othercases.append(( tuple((round(0.0254*x,2),round(0.0254*y,2),c) for x, y, c in items), False))
                    else:
                        othercases.append((items, None))



    cases += othercases
    placedrawer = True
    for stenen, inch in cases:
        if inch is None:
            print('>>> {}({!r})'.format(f.__name__, stenen), file=inFile)
        else:
            print('>>> {}({!r}, inch={!r})'.format(f.__name__, stenen, inch), file=inFile)

        try:
            if inch is None:
                result = f(stenen)
            else:
                result = f(stenen, inch=inch)
            if placedrawer:
                placedrawer = False
                print(drawcurl, file=inFile)

            print('''
<OUTPUTPROCESSOR>
DrawCurl({!r}, {!r})
</OUTPUTPROCESSOR>'''.format(stenen, inch).strip(), file=inFile)

            print(repr(result), file=inFile, end='\n\n')
        except AssertionError as ae:
            print('Traceback (most recent call last):', file=inFile)
            print('AssertionError: {}'.format(str(ae)), file=inFile, end='\n\n')

num = 1
f = solution.validPositions
print(settings.format(tabname=f.__name__, add='').strip(), file=open(join('..', 'evaluation', '{}.out'.format(num)), 'w'))
with open(join('..', 'evaluation', '{}.in'.format(num)), 'w') as inFile:
    staticcases = [
            ([(20.0, 10.0, 'R'), (25.0, 22.0, 'Y'), (42.0, 37.0, 'R')], None),
            ([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'Y')], None),
            ([(20.0, 10.0, 'R'), (25.0, 22.0, 'R'), (42.0, 37.0, 'R')], None),
            ]

    cases = staticcases


    def genPoint(low=0, high=100):
        dist = (high - low) * random.random() + low
        phi = 2 * pi * random.random()
        x, y = rotate(dist, phi)
        return x, y

    altcases = []


    for meter in (False, True):
        for status in (True, False):
            othercases = []
            while len(othercases) < 10:
                nrItems = random.randint(6, 12)
                stones = [genPoint(0, 80) + (random.choice('RY'),) for _ in range(nrItems)]    
                if meter:
                    stones = [(round(0.0254*x,2),round(0.0254*y,2),c) for x, y, c in stones]
                    inch = False
                else:
                    inch = None

                if f(stones, inch=True if inch is None else inch) == status:
                    othercases.append((stones, inch))

            altcases += othercases

    random.shuffle(altcases)
    for meter in (False, True):
        for truecolor in 'RY':
            success = False
            while not success:
                stones = [genPoint(0, 80) + ('RY'[ii%2],) for ii in range(10)]
                if meter:
                    stones = [(round(0.0254*x,2),round(0.0254*y,2),c) for x, y, c in stones]
                    inch = False
                else:
                    inch = None

                success = f(stones, inch=True if inch is None else inch)
                if success:
                    stones = [(x, y, truecolor) for x, y, c in stones]
                    x, y, col = stones[-1]
                    stones[-1] = (x, y, 'R' if col == 'Y' else 'Y')
                    random.shuffle(stones)
                    altcases.append((stones, inch))


    cases += altcases

    placedrawer = True
    for stenen, inch in cases:
        if inch is None:
            print('>>> {}({!r})'.format(f.__name__, stenen), file=inFile)
        else:
            print('>>> {}({!r}, inch={!r})'.format(f.__name__, stenen, inch), file=inFile)

        try:
            if inch is None:
                result = f(stenen)
            else:
                result = f(stenen, inch=inch)
            if placedrawer:
                placedrawer = False
                print(drawcurl, file=inFile)

            print('''
<OUTPUTPROCESSOR>
DrawCurl({!r}, {!r})
</OUTPUTPROCESSOR>'''.format(stenen, inch).strip(), file=inFile)

            print(repr(result), file=inFile, end='\n\n')
        except AssertionError as ae:
            print('Traceback (most recent call last):', file=inFile)
            print('AssertionError: {}'.format(str(ae)), file=inFile, end='\n\n')


