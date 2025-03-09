from window import Window
from maze import Maze

win = Window(800, 600)

maze = Maze(100, 100, 5, 5, 20, 20, win)


win.wait_for_close()

