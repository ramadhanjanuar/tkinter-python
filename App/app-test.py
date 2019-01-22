# NPM  : 0616103014
# Nama : Mochammad Ramadhan Januar Hidayat

from tkinter import *

class Tugas(object):
    """docstring for Tugas."""
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.parent.geometry("740x550")

        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, relief=SUNKEN)
        mainFrame.pack(fill=BOTH, side=LEFT )
        self.mainFrame = mainFrame

        mainFrameR = Frame(mainFrame, bd=1, bg="white")
        mainFrameR.pack(fill=BOTH, expand=YES, side=RIGHT)

        self.canvas = Canvas(mainFrameR, bg="white")
        self.canvas.pack(fill=BOTH, expand=YES, side=RIGHT, padx=10, pady=10)

        frameButton = Frame(mainFrame, bd=10,)
        frameButton.pack(fill=BOTH)

        Pilih = Label(frameButton, text="PILIH SALAH SATU", font = "Helvetica 16 bold italic").grid(row=0, column=0, sticky=E+W, padx=50, pady=10)
        btnGaris = Button(frameButton, text="Garis", relief=GROOVE, command= lambda *args : self.inputan(1) ).grid(row=1, column=0, sticky=E+W, padx=50, pady=10)
        btnElips = Button(frameButton, text="Elips", relief=GROOVE).grid(row=3, column=0, sticky=E+W, padx=50, pady=10)
        btnLingk = Button(frameButton, text="Lingkaran", relief=GROOVE ).grid(row=2, column=0, sticky=E+W, padx=50, pady=10)

        frameInputan = Frame(self.mainFrame, bd=10, )
        frameInputan.pack(fill=BOTH)
        self.frameInputan = frameInputan


    def inputan(self, pil):
        frameInputan = self.frameInputan
        print(pil)
        Label(frameInputan, text="Enter X1 : ").grid(row = 0, column=0)
        self.x1Var = Entry(frameInputan)
        self.x1Var.grid(row = 0, column = 1)

        Label(frameInputan, text="Enter Y1 : ").grid(row = 1, column=0)
        self.y1Var = Entry(frameInputan)
        self.y1Var.grid(row = 1, column = 1)


        Label(frameInputan, text ="Enter X2 : ").grid(row = 2, column = 0)
        self.x2Var = Entry(frameInputan)
        self.x2Var.grid(row = 2, column = 1)

        Label(frameInputan, text ="Enter Y2 : ").grid(row = 3, column = 0)
        self.y2Var = Entry(frameInputan)
        self.y2Var.grid(row = 3, column = 1)

        Label(frameInputan, text ="Pilih Method : ").grid(row = 4, column = 0)

        self.var = StringVar(frameInputan)
        self.var.set("---") # default value

        w = OptionMenu(frameInputan, self.var, "DDA", "BRESENHAM")
        w.grid(row=4, column = 1, sticky=E+W, padx=1)

        btnMetod = Button(frameInputan, text="Pilih", command=self.choices ).grid(row=4, column=2)

        btnClear = Button(frameInputan, text = "Bersihkan Kanvas", comman=self.clearCanvas)
        btnClear.grid(row = 5, column = 1, sticky =E+W, padx=1)

    def choices(self, event=None):
        choice = self.var.get()
        if choice == 'DDA':
            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.dda)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)
        elif choice =='BRESENHAM' :
            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.garisbresenham)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)


    #fungsi membuat garis menggunakan algoritma digital differential analizer
    def dda(self, event= None):
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


    #fungsi membuat garis menggunakan algoritma bresenham
    def garisbresenham(self, event = None):
        x1 = int(self.x1Var.get())
        x2 = int(self.x2Var.get())
        y1 = int(self.y1Var.get())
        y2 = int(self.y2Var.get())

        x = x1
        y = y1

        Dy = y2 - y1
        Dx = x2 - x1
        P = (2*Dy)-Dx

        while x <= x2:
            if P < 0 :
                x += 1
                P += P + (2*Dy)
                self.canvas.create_text(x, y, text=".", tag="line")
            else :
                x += 1
                y += 1
                P += (2*Dy) - (2*Dx)
                self.canvas.create_text(x, y, text=".", tag="line")


    #membersihkan kanvas
    def clearCanvas(self):
        self.canvas.delete("line")

    def onKeluar(self):
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()

    aplikasi = Tugas(root, "Tugas Grafkom - 0616103014 - Mochammad Ramadhan Januar H")

    root.mainloop()
