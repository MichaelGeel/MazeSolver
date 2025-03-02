from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2


    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=color, width=2)


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
        # if isinstance(line, Line):
        line.draw(self.canvas, color)
        # raise Exception(f"Expected object of class 'Line', got object of type {type(line)}")