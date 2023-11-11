import math

#returns theta and distance in tuple, finds angle between player and object, x/y is player, x2/y2 is object
def direction(x, y, x2, y2):

    #Flip y-axis of objects for accurate grid and direction
    dist = 0

    #Switch y values in case of different y grids
    if (y > 560) and (y2 < 560) or (y < 560) and (y2 > 560):
        #switch y-vals
        t = y
        y = y2
        y2 = t

        #calculate theta
        xf = x-x2
        yf = y-y2

        #1st quad 0-90, 2nd quad 90-180, 3rd quad -180 - -90, 4th quad -90-0
        theta = math.degrees(math.atan2(yf, xf))
        r = math.sqrt((xf ** 2) + (yf ** 2))

        return theta, r

    if y > 560:
        dist = 1120 - y
        y = 560 + dist

    if y2 > 560:
        dist = 1120 - y2
        y2 = 560 + dist

    if y < 560:
        dist = (560) - y
        y += (2 * dist)

    if y2 < 560:
        dist = (560) - y2
        y2 += (2 * dist)

    xf = x-x2
    yf = y-y2
   
    #1st quad 0-90, 2nd quad 90-180, 3rd quad -180 - -90, 4th quad -90-0
    theta = math.degrees(math.atan2(yf, xf))
    r = math.sqrt((xf ** 2) + (yf ** 2))
    
    return theta, r

        

def gravity(distance, m1, m2, gravity):

    velocity = gravity * (m1*m2) / (distance ** 2)

    return velocity