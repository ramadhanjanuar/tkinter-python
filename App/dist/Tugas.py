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

        self.canvas = Canvas(mainFrameR, bg="white", scrollregion=(0,0,500,500 ))
        self.canvas.pack(fill=BOTH, expand=YES, side=RIGHT, padx=10, pady=10)

        frameButton = Frame(mainFrame, bd=10,)
        frameButton.pack(fill=BOTH)

        Pilih = Label(frameButton, text="PILIH SALAH SATU", font = "Helvetica 16 bold italic").grid(row=0, column=0, sticky=E+W, padx=50, pady=10)
        btnGaris = Button(frameButton, text="Garis", relief=GROOVE, command= lambda *args : self.inputan(1) ).grid(row=1, column=0, sticky=E+W, padx=50, pady=10)
        btnElips = Button(frameButton, text="Elips", relief=GROOVE,command= lambda *args : self.inputan(2)).grid(row=3, column=0, sticky=E+W, padx=50, pady=10)
        btnLingk = Button(frameButton, text="Lingkaran", relief=GROOVE,command= lambda *args : self.inputan(3) ).grid(row=2, column=0, sticky=E+W, padx=50, pady=10)

        self.frameInputan = Frame(self.mainFrame, bd=10, )
        self.frameInputan.pack(fill=BOTH)
        self.pilMtd = None


    def input(self):
        self.frame = self.frameInputan
        self.label1 = Label(self.frame)
        self.label1.grid(row = 0, column=0)
        self.Var1 = Entry(self.frame)
        self.Var1.grid(row = 0, column = 1)

        self.label2 = Label(self.frame)
        self.label2.grid(row = 1, column=0)
        self.Var2 = Entry(self.frame)
        self.Var2.grid(row = 1, column = 1)

        self.label3 = Label(self.frame)
        self.label3.grid(row = 2, column = 0)
        self.Var3 = Entry(self.frame)
        self.Var3.grid(row = 2, column = 1)

        self.label4 = Label(self.frame)
        self.label4.grid(row = 3, column = 0)
        self.Var4 = Entry(self.frame)
        self.Var4.grid(row = 3, column = 1)


    def inputan(self, pil):
        self.input()
        if pil == 1:
            self.input()
            self.label1['text'] = 'Enter X1 :'
            self.label2['text'] = 'Enter Y1 :'
            self.label3['text'] = 'Enter X2 :'
            self.label4['text'] = 'Enter Y2 :'

            self.pilMtd = True
            self.metod = Label(self.frameInputan, text ="Pilih Method : ")
            self.metod.grid(row = 4, column = 0)
            self.var = StringVar(self.frameInputan)
            self.var.set("---") # default value

            self.w = OptionMenu(self.frameInputan, self.var, "DDA", "BRESENHAM")
            self.w.grid(row=4, column = 1, sticky=E+W, padx=1)

            self.btnMetod = Button(self.frameInputan, text="Pilih", command=self.choices )
            self.btnMetod.grid(row=4, column=2)
        elif pil == 2:
            self.input()
            if self.pilMtd:
                self.metod.grid_remove()
                self.w.grid_remove()
                self.btnMetod.grid_remove()
                self.pilMtd = False

            self.label1.configure(text = "Enter X  : ")
            self.label2.configure(text = "Enter Y  : ")
            self.label3.configure(text = "Enter rx : ")
            self.label4.configure(text = "Enter ry : ")

            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.elips)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)
        else :
            self.input()
            if self.pilMtd:
                self.metod.grid_remove()
                self.w.grid_remove()
                self.btnMetod.grid_remove()
                self.pilMtd = False

            self.label1['text'] = "Enter X : "
            self.label2['text'] = "Enter Y : "
            self.label3['text'] = "Enter r : "
            self.label4.configure(state=DISABLED)
            self.Var4.configure(state=DISABLED)


            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.lingkaran)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)

        btnClear = Button(self.frameInputan, text = "Bersihkan Kanvas", comman=self.clearCanvas)
        btnClear.grid(row = 5, column = 1, sticky =E+W, padx=1)

    def choices(self, event=None):
        choice = self.var.get()
        if choice == 'DDA':
            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.dda)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)
        elif choice =='BRESENHAM' :
            btnDrawLine = Button(self.frameInputan, text = "Gambar", command=self.garisbresenham)
            btnDrawLine.grid(row = 5, column = 0, sticky =E+W, padx=1)

    #membuat garis menggunakan algoritma digital differential analizer
    def dda(self, event= None):
        x1 = int(self.Var1.get())
        x2 = int(self.Var3.get())
        y1 = int(self.Var2.get())
        y2 = int(self.Var4.get())

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
            print(steps, x, y)

    #membuat garis menggunakan algoritma bresenham
    def garisbresenham(self, event = None):
        x1 = int(self.Var1.get())
        x2 = int(self.Var3.get())
        y1 = int(self.Var2.get())
        y2 = int(self.Var4.get())

        x = x1
        y = y1

        Dy = abs(y2 - y1)
        Dx = abs(x2 - x1)
        P = abs((2*Dy)-Dx)

        if x1 < x2:
            while x < x2:
                if P < 0 :
                    x += 1
                    P += (2*Dy)
                    self.canvas.create_text(x, y, text=".", tag="line")
                else :
                    x += 1
                    y += 1
                    P += (2*Dy) - (2*Dx)
                    self.canvas.create_text(x, y, text=".", tag="line")

                print(P, x, y)
        else :
            while x > x2:
                if P < 0 :
                    x -= 1
                    P += (2*Dy)
                    self.canvas.create_text(x, y, text=".", tag="line")
                else :
                    x -= 1
                    y += 1
                    P += (2*Dy) - (2*Dx)
                    self.canvas.create_text(x, y, text=".", tag="line")

                print(P, x, y)

    #membuat lingkaran dengan algoritma bresenham
    def lingkaran(self):
        xc = int(self.Var1.get())
        yc = int(self.Var2.get())
        r = int(self.Var3.get())
        x = 0;
        y = r
        P = 1 - r
        while x < y:
            self.canvas.create_text(xc + x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc + x, yc - y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc - y, text=".", tag="line")
            self.canvas.create_text(xc + y, yc + x, text=".", tag="line")
            self.canvas.create_text(xc - y, yc + x, text=".", tag="line")
            self.canvas.create_text(xc + y, yc - x, text=".", tag="line")
            self.canvas.create_text(xc - y, yc - x, text=".", tag="line")
            x += 1
            if P < 1:
                P += (2 * x) + 1
            else:
                y -= 1
                P += + (2 * x) + 1 - (2 * y)

    #membuat elips memnggunakan algoritma bresenham
    def elips(self):
        xc = float(self.Var1.get())
        yc = float(self.Var2.get())
        rx = float(self.Var3.get())
        ry = float(self.Var4.get())

        rx_sqr = rx ** 2
        ry_sqr = ry ** 2
        x = 0
        y = ry

        pX = 0
        pY = 2 * rx_sqr * y

        #Reg 1
        PReg1 = round(ry_sqr - (rx_sqr * ry) + (1 / 4 * rx_sqr))
        while pX < pY:
            x+=1
            pX += (2 * ry_sqr)
            if PReg1 >= 0:
                y-=1
                pY -= (2 * rx_sqr)
                PReg1 += ry_sqr + pX - pY
            else:
                PReg1 += ry_sqr + pX

            self.canvas.create_text(xc + x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc + x, yc - y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc - y, text=".", tag="line")

        #Reg 2
        PReg2 = round(ry_sqr * ((x + 1 / 2) ** 2) + rx_sqr * ((y - 1) ** 2) - rx_sqr * ry_sqr)
        while y > 0:
            y-=1
            pY -= (2 * rx_sqr)
            if PReg2 <= 0:
                x+=1
                pX += (2 * ry_sqr)
                PReg2 += rx_sqr + pX - pY
            else:
                PReg2 += rx_sqr - pY

            self.canvas.create_text(xc + x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc + y, text=".", tag="line")
            self.canvas.create_text(xc + x, yc - y, text=".", tag="line")
            self.canvas.create_text(xc - x, yc - y, text=".", tag="line")



    #membersihkan kanvas
    def clearCanvas(self):
        self.canvas.delete("line")

    def onKeluar(self):
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()

    aplikasi = Tugas(root, "Tugas Grafkom - 0616103014 - Mochammad Ramadhan Januar H")

    root.mainloop()
