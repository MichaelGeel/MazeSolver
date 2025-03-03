from window import Window
from shapes import Cell, Point
import time


class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()


    def __create_cells(self):
        self.__cells = []
        for i in range(0, self.__num_cols):
            col_list = []
            for j in range(0, self.__num_rows):
                col_list.append(Cell(self.__win))
            self.__cells.append(col_list)
        for i in range(0, self.__num_cols):
            for j in range(0, self.__num_rows):
                self.__draw_cell(i, j)


    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        p1 = Point(self.__x1 + (self.__cell_size_x*i), self.__y1 + (self.__cell_size_y*j))
        p2 = Point(self.__x1 + (self.__cell_size_x*(i+1)), self.__y1 + (self.__cell_size_y*(j+1)))
        cell.draw(p1, p2)
        self.__animate()


    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
