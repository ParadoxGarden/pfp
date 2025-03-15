import drawsvg as dw
import math
import time
 
def draw_clock(radius:int,fill, accent,include_seconds:bool=False, smooth_hands:bool=True, clocktime:time.struct_time=time.localtime())->dw.Drawing:
    d:dw.Drawing = dw.Drawing(2*radius,2*radius, origin='center')
    d.append(dw.Rectangle(-radius,-radius,2*radius,2*radius,fill=fill))
    d.append(dw.Circle(0,0,radius, fill=fill, stroke_width=20,stroke=fill))
    for i in range(0,360,30):
        rad = math.radians(i)
        # time sectional markings
        l:dw.Line = dw.Line(
            radius * math.cos(rad),
            radius * math.sin(rad),
            (radius - (radius / 6)) * math.cos(rad),
            (radius - (radius / 6)) * math.sin(rad),
            stroke=accent,stroke_width=25)
        d.append(l)
    clocktime = time.localtime()
    if smooth_hands:
        minfrac:float = clocktime.tm_min / 60
        secfrac:float = clocktime.tm_sec / 60
        hourrad = math.radians(360 / 12 * (clocktime.tm_hour + minfrac))
        minrad = math.radians(360 / 60 * (clocktime.tm_min + secfrac))
        secrad = math.radians(360 / 60 * clocktime.tm_sec)
    else:
        hourrad = math.radians(360 / 12 * clocktime.tm_hour)
        minrad = math.radians(360 / 60 * clocktime.tm_min)
        secrad = math.radians(360 / 60 * clocktime.tm_sec)
    # seconds hand (if shown)
    if include_seconds:
        secrad = math.radians(360 / 60 * clocktime.tm_sec)
        l = dw.Line(
            0,0,
            (radius - (radius / 6)) * math.sin(secrad), 
            -(radius - (radius / 6)) * math.cos(secrad),
            stroke="red",stroke_width=10)
        d.append(l)
    # minute hand
    l = dw.Line(
        0,0,
        (radius - (radius / 5)) * math.sin(minrad), 
        -(radius - (radius / 5)) * math.cos(minrad),
        stroke="grey",stroke_width=30)
    d.append(l)
    # hour hand
    l = dw.Line(
        0,0,
        (radius - (radius / 2)) * math.sin(hourrad), 
        -(radius - (radius / 2)) * math.cos(hourrad),
        stroke="black",stroke_width=40)
    d.append(l)
    d.append(dw.Circle(0,0,radius/40, fill=accent))
    return d

# group gradient stuff for future use
def make_gradient()->dw.LinearGradient:
    # gradient definition
    grad = dw.LinearGradient(-150,-150,150,150)
    grad.add_stop(-150,"mistyrose")
    grad.add_stop(150,"thistle")
    return grad

# defines default pfp params
def draw_default_clock()->dw.Drawing:
    grad: dw.LinearGradient = make_gradient()
    d = draw_clock(1000, grad,"black", False, True)
    return d


if __name__ == "__main__":
    d:dw.Drawing = draw_default_clock()
    d.save_svg("pfp.svg")
    d.save_png("pfp.png")
    
    
