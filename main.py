from window import Window
from shapes import Point, Cell

win = Window(800, 600)

p1 = Point(100, 100)
p2 = Point(120, 120)
p3 = Point(100, 120)
p4 = Point(120, 140)

c1 = Cell(win=win)
c1.draw(p1, p2)

c2 = Cell(win=win)
c2.draw(p3, p4)

c1.draw_move(c2, True)


win.wait_for_close()