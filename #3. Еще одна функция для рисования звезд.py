import turtle
t = turtle.Pen()
t.reset()
def draw_star(size, points, filled):
    if filled == True:
        t.begin_fill()
    angle = 360 / points
    for x in range(0, points):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180-(angle * 2))
    if filled == True:
        t.end_fill()

t.color(0.9,0.75,0)
draw_star(100, 10, True)
t.color(0,0,0)
draw_star(100, 10, False)
t.up()
t.color(1,1,1)
t.forward(200)
