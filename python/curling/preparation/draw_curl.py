class DrawCurl(OutputProcessor):

    def __init__(self, stonelist, inch, **kwargs):
        
        # call initialization method of base class
        super().__init__(**kwargs)
        
        self.stonelist = stonelist
        self.inch = inch

    def renderOutput(self, **kwargs):
        
        if self.getStatus() == 'AC':
            return
 
        from math import pi
        from io import StringIO
        colormap = {'R' : '#C81A2D', 'Y' : '#EBD141'}
        colormap['G'] = colormap['Y']

        outfile = StringIO()
        dim = (200, 200)
        center = [x/2 for x in dim]
        maxradius = min(dim) // 2
        maxradius = round(0.8*maxradius)
        ticksperinch = maxradius/(12*6)
        middleradius = round((2/3)*maxradius)
        smallradius = round((1/3)*maxradius)
        innerradius = round((1/12)*maxradius)
        stoneradius = (36 / (2 * pi)) * ticksperinch

        print('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}">'.format(*dim), file=outfile)
        print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="#F35A61" />.'.format(*center, maxradius), file=outfile)
        print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="#FFFFFF" />.'.format(*center, middleradius), file=outfile)
        print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="#6A7FBB" />.'.format(*center, smallradius), file=outfile)
        print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="#FFFFFF" />.'.format(*center, innerradius), file=outfile)
        print('<line x1="{centerx}" y1="0" x2="{centerx}" y2="{dimy}" style="stroke:rgb(105,105,105);stroke-width:2;stroke-opacity:0.2" />'.format(centerx=center[0], dimy=dim[1]), file=outfile)
        print('<line x1="0" y1="{centery}" x2="{dimx}" y2="{centery}" style="stroke:rgb(105,105,105);stroke-width:2;stroke-opacity:0.2" />'.format(centery=center[1], dimx=dim[0]), file=outfile)

        def placeStone(x, y, color='R'):
            stonecoord = tuple(ticksperinch*r + c for r, c in zip((x, y), center))
            print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="#000000" />.'.format(*stonecoord, stoneradius), file=outfile)
            print('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="0" fill="{}" />.'.format(*stonecoord, 0.7*stoneradius, colormap[color]), file=outfile)


        for x, y, color in self.stonelist:
            if self.inch is False:
                x, y = (r/0.0254 for r in (x, y))

            placeStone(x, -y, color)

        print('</svg>', file=outfile)

        self.addMessage(outfile.getvalue(), escape=False, plain=True)
