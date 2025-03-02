from window import Window, Point, Line

win = Window(800, 600)

p1 = Point(0, 0)
p2 = Point(100, 200)
l1 = Line(p1, p2)
win.draw_line(l1, "red")


win.wait_for_close()