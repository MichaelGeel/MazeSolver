from tkinter import Tk, BOTH, Canvas

## Not creating a window using Tk here, creating a Window class that inherits FROM Tk.

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.config(width=width, height=height)
        self.__root.title("MazeSolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(master=self.__root, background="blue")
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