from window import Window
from shapes import Cell, Point
import time
import random


class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
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
        if seed:
            random.seed(self.seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            vals_list = []
            if i < self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    vals_list.append("right")
                if i > 0:
                    if not self._cells[i-1][j].visited:
                        vals_list.append("left")
            if j < self._num_rows-1:
                if not self._cells[i][j+1].visited:
                    vals_list.append("down")
                if j > 0:
                    if not self._cells[i][j-1].visited:
                        vals_list.append("up")
            if len(vals_list) == 0:
                self._draw_cell(i, j)
                return
            else:
                chosen_cell = random.choice(vals_list)
                
                match chosen_cell:
                    case "up":
                        self._cells[i][j].has_top_wall = False
                        self._cells[i][j-1].has_bottom_wall = False
                        self._break_walls_r(i, j-1)
                    case "down":
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[i][j+1].has_top_wall = False
                        self._break_walls_r(i, j+1)
                    case "left":
                        self._cells[i][j].has_left_wall = False
                        self._cells[i-1][j].has_right_wall = False
                        self._break_walls_r(i-1, j)
                    case "right":
                        self._cells[i][j].has_right_wall = False
                        self._cells[i+1][j].has_left_wall = False
                        self._break_walls_r(i+1, j)

    def _reset_cells_visited(self):
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        result = self._solve_r(0, 0)
        return result
    
    def _solve_r(self, i, j):
        # Depth First
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        directions = ["up", "down", "left", "right"]
        for direction in directions:
            match direction:
                case "up":
                    if self._cells[i][j].has_top_wall == False and j > 0 and self._cells[i][j-1].visited == False:
                        self._cells[i][j].draw_move(self._cells[i][j-1])
                        res = self._solve_r(i, j-1)
                        if res == True:
                            return True
                        self._cells[i][j].draw_move(self._cells[i][j-1], True)
                case "down":
                    if self._cells[i][j].has_bottom_wall == False and j < self._num_rows-1 and self._cells[i][j+1].visited == False:
                        self._cells[i][j].draw_move(self._cells[i][j+1])
                        res = self._solve_r(i, j+1)
                        if res == True:
                            return True
                        self._cells[i][j].draw_move(self._cells[i][j+1], True)
                case "left":
                    if self._cells[i][j].has_left_wall == False and i > 0 and self._cells[i-1][j].visited == False:
                        self._cells[i][j].draw_move(self._cells[i-1][j])
                        res = self._solve_r(i-1, j)
                        if res == True:
                            return True
                        self._cells[i][j].draw_move(self._cells[i-1][j], True)
                case "right":
                    if self._cells[i][j].has_right_wall == False and i < self._num_cols-1 and self._cells[i+1][j].visited == False:
                        self._cells[i][j].draw_move(self._cells[i+1][j])
                        res = self._solve_r(i+1, j)
                        if res == True:
                            return True
                        self._cells[i][j].draw_move(self._cells[i+1][j], True)
        return False