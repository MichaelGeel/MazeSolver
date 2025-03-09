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
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False

    def draw(self, point_1: Point, point_2: Point):
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        if self.has_left_wall:
            l_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "black")
        else:
            l_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "white")
        if self.has_right_wall:
            l_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "black")
        else:
            l_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "white")
        if self.has_top_wall:
            l_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self._win:
                l_line.draw(self._win.canvas, "black")
        else:
            l_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self._win:
                l_line.draw(self._win.canvas, "white")
        if self.has_bottom_wall:
            l_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "black")
        else:
            l_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self._win:
                l_line.draw(self._win.canvas, "white")

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if undo:
            color = "red"
        this_mid_x = (self._x1 + self._x2)//2
        this_mid_y = (self._y1 + self._y2)//2
        to_mid_x = (to_cell._x1 + to_cell._x2)//2
        to_mid_y = (to_cell._y1 + to_cell._y2)//2
        line = Line(Point(this_mid_x, this_mid_y), Point(to_mid_x, to_mid_y))
        if self._win:
            line.draw(self._win.canvas, color)