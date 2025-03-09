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
            win = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):
        self._cells = []
        for i in range(0, self._num_cols):
            col_list = []
            for j in range(0, self._num_rows):
                col_list.append(Cell(self._win))
            self._cells.append(col_list)
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        p1 = Point(self._x1 + (self._cell_size_x*i), self._y1 + (self._cell_size_y*j))
        p2 = Point(self._x1 + (self._cell_size_x*(i+1)), self._y1 + (self._cell_size_y*(j+1)))
        cell.draw(p1, p2)
        self._animate()


    def _animate(self):
        if self._win:
            self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
