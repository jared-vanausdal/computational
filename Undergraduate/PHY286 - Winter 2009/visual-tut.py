import visual

floor = visual.box(pos=(0,0,0),length=4,height=0.5,width=4, color=visual.color.blue)
ball = visual.sphere(pos=(0,4,0), radius=1, color=visual.color.red)
ball.velocity = visual.vector(0,-1,0)
dt = 0.01

while 1:
    visual.rate(100)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.y < ball.radius:
        ball.velocity.y = -ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
