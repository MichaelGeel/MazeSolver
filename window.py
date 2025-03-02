from tkinter import Tk, BOTH, Canvas
from shapes import Line


class Window():
    def __init__(self, w: int, h: int):
        self.__root = Tk()
        self.__root.config(width=w, height=h)
        self.__root.title("MazeSolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(master=self.__root, background="blue", width=w, height=h)
        self.canvas.pack()
        self.running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()


    def close(self):
        self.running = False


    def draw_line(self, line: Line, color: str):
        line.draw(self.canvas, color)