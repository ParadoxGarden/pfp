import drawsvg as dw
import math
import time
 
def draw_clock(radius:int,fill, accent,include_seconds:bool=False)->None:
    d = dw.Drawing(2*radius,2*radius, origin='center')
    def add_to_drawing(stroke:dw.DrawingElement)->None:
        d.append(stroke)
    add_to_drawing(dw.Circle(0,0,radius, fill=fill, stroke_width=20,stroke=accent))
    for i in range(0,360,30):
        rad = math.radians(i)
        # time sectional markings
        l = dw.Line(
            radius * math.cos(rad),
            radius * math.sin(rad),
            (radius - (radius / 6)) * math.cos(rad),
            (radius - (radius / 6)) * math.sin(rad),
            stroke=accent,stroke_width=25)
        add_to_drawing(l)
    # minute hand
    curtime = time.localtime()
    minrad = math.radians(360 / 60 * curtime.tm_min)
    l = dw.Line(
        0,0,
        (radius - (radius / 5)) * math.sin(minrad), 
        -(radius - (radius / 5)) * math.cos(minrad),
        stroke="grey",stroke_width=30)
    add_to_drawing(l)
    # hour hand
    hourrad = math.radians(360 / 12 * curtime.tm_hour)
    l = dw.Line(
        0,0,
        (radius - (radius / 2)) * math.sin(hourrad), 
        (radius - (radius / 2)) * math.cos(hourrad),
        stroke="black",stroke_width=40)
    add_to_drawing(l)

    if include_seconds:
        secrad = math.radians(360 / 60 * curtime.tm_sec)
        l = dw.Line(
            0,0,
            (radius - (radius / 2)) * math.sin(secrad), 
            -(radius - (radius / 2)) * math.cos(secrad),
            stroke="red",stroke_width=10)
        add_to_drawing(l)
    
    add_to_drawing(dw.Circle(0,0,radius/40, fill=accent))
    return d
# gradient definition
grad = dw.LinearGradient(-150,-150,150,150)
grad.add_stop(-150,"mistyrose")
grad.add_stop(150,"thistle")

#define pfp
d = draw_clock(1000, grad,"black")

d.save_png("test.png")
d.save_svg("test.svg")