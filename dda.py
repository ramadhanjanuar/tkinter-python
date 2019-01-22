from tkinter import *

class DDALineDrawTK(object):
    """docstring for DDALineDrawTK."""
    def __init__(self, parent, title):

        self.parent = parent
        self.parent.title(title)

        self.canvas = Canvas(self.parent, width = 500, height = 500, bg="white")
        self.canvas.pack()

        frame = Frame(self.parent)
        frame.pack()

        Label(frame, text="Enter X1 : ").grid(row = 1, column=1)
        self.x1Var = Entry(frame)
        self.x1Var.grid(row = 1, column = 2)
        Label(frame, text="Enter Y1 : ").grid(row = 1, column=3)
        self.y1Var = Entry(frame)
        self.y1Var.grid(row = 1, column = 4)


        Label(frame, text ="Enter X2 : ").grid(row = 2, column = 1)
        self.x2Var = Entry(frame)
        self.x2Var.grid(row = 2, column = 2)
        Label(frame, text ="Enter Y2 : ").grid(row = 2, column = 3)
        self.y2Var = Entry(frame)
        self.y2Var.grid(row = 2, column = 4)


        btnDrawLine = Button(frame, text = "Draw Line", command = self.drawLine)
        btnDrawLine.grid(row = 3, column = 1)
        btnClear = Button(frame, text = "Clear Canvas", command = self.clearCanvas)
        btnClear.grid(row = 3, column = 2)



    #membuat garis
    def drawLine(self):
        x1 = int(self.x1Var.get())
        x2 = int(self.x2Var.get())
        y1 = int(self.y1Var.get())
        y2 = int(self.y2Var.get())

        dx = x2-x1
        dy = y2-y1

        x = x1
        y = y1

        steps = dx if abs(dx) > abs(dy) else dy

        Xr = dx / steps
        Yr = dy / steps

        i = 1

        while i < steps  :
            x += Xr
            y += Yr
            self.canvas.create_text(x, y, text=".", tag="line")
            i += 1

    #membersihkan kanvas
    def clearCanvas(self):
        self.canvas.delete("line")


if __name__ == '__main__':
    root = Tk()

    aplikasi = DDALineDrawTK(root, "DDA")

    root.mainloop()
