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


        btnDrawLine = Button(frame, text = "Draw Line", command = lambda *args : self.membuatHurufA(int(self.x1Var.get()), int(self.x2Var.get()), int(self.y1Var.get()), int(self.y2Var.get())))
        btnDrawLine.grid(row = 3, column = 1)
        btnClear = Button(frame, text = "Clear Canvas", command = self.clearCanvas)
        btnClear.grid(row = 3, column = 2)



    #membuat garis menggunakan algoritma dda
    def fungsigaris(self, x1, x2, y1, y2):
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

    #membuat garis dengan algoritma bresenham
    def fungsigariss(self, x1, x2, y1, y2):


        x = int(x1)
        y = int(y1)

        Dy = int(y2 - y1)
        Dx = x2 - x1
        P = (2*Dy)-Dx

        k = 0
        while x <= x2 and y <= y2:
            if P < 0 :
                x += 1
                P += (2*Dy)
                self.canvas.create_text(x, y, text=".", tag="line")
            elif P >= 0 :
                x += 1
                y += 1
                P += (2*Dy) - (2*Dx)
                self.canvas.create_text(x, y, text=".", tag="line")

            k+=1

    #membersihkan kanvas
    def clearCanvas(self):
        self.canvas.delete("line")

    def membuatHurufA(self, x1, x2, y1, y2):
        a = x1
        b = x2
        c = y1
        d = y2
        return self.garisA(a, b, c, d),self.garisB(a, b, c, d),self.garisC(a, b, c, d),self.garisD(a, b, c, d),\
        self.garisE(a, b, c, d),self.garisF(a, b, c, d),self.garisG(a, b, c, d),self.garisH(a, b, c, d), \
        self.garisI(a, b, c, d),self.garisJ(a, b, c, d),self.garisK(a, b, c, d),self.garisL(a, b, c, d)

    #membuat garis bagian A
    def garisA(self, a, b, c, d):
        x1 = a
        x2 = a + ((b*15.39)//100)
        y1 = d
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian B
    def garisB(self, a, b, c, d):
        x1 = a + ((b * 19.23)//100)
        x2 = a + ((b*15.39)//100)
        y1 = d - ((d*16.67)//100)
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian C
    def garisC(self, a, b, c, d):
        x1 = a + ((b * 19.23)//100)
        x2 = b - ((b*19.23)//100)
        y1 = d - ((d*16.67)//100)
        y2 = d - ((d*16.67)//100)
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian D
    def garisD(self, a, b, c, d):
        x1 = b - ((b * 19.23)//100)
        x2 = b - ((b*15.39)//100)
        y1 = d - ((d*16.67)//100)
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian E
    def garisE(self, a, b, c, d):
        x1 = b - ((b*15.39)//100)
        x2 = b
        y1 = d
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian F
    def garisF(self, a, b, c, d):
        x1 = b - ((b*23.07)//100)
        x2 = b
        y1 = c
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian G
    def garisG(self, a, b, c, d):
        x1 = a + ((b*23.07)//100)
        x2 = a
        y1 = c
        y2 = d
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian H
    def garisH(self, a, b, c, d):
        x1 = a + ((b*23.07)//100)
        x2 = b - ((b*23.07)//100)
        y1 = d - ((d*27.77)//100)
        y2 = d - ((d*27.77)//100)
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian I
    def garisI(self, a, b, c, d):
        x1 = b - ((b*28.84)//100)
        x2 = b - ((b*23.07)//100)
        y1 = c + ((d*11.11)//100)
        y2 = d - ((d*27.77)//100)
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian J
    def garisJ(self, a, b, c, d):
        x1 = a + ((b*28.84)//100)
        x2 = a + ((b*23.07)//100)
        y1 = c + ((d*11.11)//100)
        y2 = d - ((d*27.77)//100)
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian K
    def garisK(self, a, b, c, d):
        x1 = a + ((b*23.07)//100)
        x2 = b - ((b*23.07)//100)
        y1 = c
        y2 = c
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)

    #membuat garis bagian L
    def garisL(self, a, b, c, d):
        x1 = a + ((b*28.84)//100)
        x2 = b - ((b*28.84)//100)
        y1 = c + ((d*11.11)//100)
        y2 = c + ((d*11.11)//100)
        print(x1,x2,y1,y2)
        return self.fungsigaris(x1, x2, y1, y2)





if __name__ == '__main__':
    root = Tk()

    aplikasi = DDALineDrawTK(root, "DDA")

    root.mainloop()
