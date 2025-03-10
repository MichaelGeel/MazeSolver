from tkinter import Tk, BOTH, Canvas
from shapes import Line


class Window():
    def __init__(self, w: int, h: int):
        self._root = Tk()
        self._root.config(width=w, height=h)
        self._root.title("MazeSolver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(master=self._root, background="white", width=w, height=h)
        self.canvas.pack()
        self.running = False


    def redraw(self):
        self._root.update_idletasks()
        self._root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()


    def close(self):
        self.running = False


    def draw_line(self, line: Line, color: str):
        line.draw(self.canvas, color)