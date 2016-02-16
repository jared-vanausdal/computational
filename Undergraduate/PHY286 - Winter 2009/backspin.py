import math
import pylab

def backspin_step(x,y,vx,vy,dt):
    
def backspin():
    v = 49
    theta = math.radians(i)
    vx = v*math.cos(theta)
    vy = v*math.sin(theta)
    x = 0
    y = 1
    dt = 0.001
    x_list = [x]
    y_list = [y]
    while y >= 0:
        x,y,vx,vy = batted_ball_rangestep(x,y,vx,vy,dt)
        x_list.append(x)
        y_list.append(y)
