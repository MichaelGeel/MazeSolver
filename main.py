from window import Window
from maze import Maze

win = Window(800, 600)

# p1 = Point(100, 100)
# p2 = Point(120, 120)
# p3 = Point(100, 120)
# p4 = Point(120, 140)

# c1 = Cell(win=win)
# c1.draw(p1, p2)

# c2 = Cell(win=win)
# c2.draw(p3, p4)

# c1.draw_move(c2, True)

maze = Maze(100, 100, 5, 5, 20, 20, win)


win.wait_for_close()