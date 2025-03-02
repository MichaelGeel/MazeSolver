from tkinter import Canvas

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


class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 20
        self.__y2 = 20
        self.__win = win

    def draw(self, point_1: Point, point_2: Point):
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y
        if self.has_left_wall:
            l_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            l_line.draw(self.__win.canvas, "black")
        if self.has_right_wall:
            l_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            l_line.draw(self.__win.canvas, "black")
        if self.has_top_wall:
            l_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            l_line.draw(self.__win.canvas, "black")
        if self.has_bottom_wall:
            l_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            l_line.draw(self.__win.canvas, "black")
