def distance(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    return ( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )**(.5)

def restart():
    global obstacles
    global y_bird
    global vy_bird
    obstacles = []
    y_bird = 135
    vy_bird = 0
