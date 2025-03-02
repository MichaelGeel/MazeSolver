from window import Window
from shapes import Point, Cell

win = Window(800, 600)

p1 = Point(100, 100)
p2 = Point(120, 120)

c1 = Cell(win=win)
c1.draw(p1, p2)


win.wait_for_close()