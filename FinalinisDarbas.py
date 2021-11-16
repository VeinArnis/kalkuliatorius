from tkinter import *
import math

main = Tk()
main.title("Kalkuliatorius")
main.geometry()

calc = Frame(main, bd=20, pady=5, bg='gray', relief=RIDGE)
calc.grid()


class Kalk:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "plus":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def deleteBS(self):
        numLen = len(txtDisplay.get())
        txtDisplay.delete(numLen - 1, 'end')
        if numLen == 1:
            txtDisplay.insert(0, "0")

    def Plus_Minus(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)


added_value = Kalk()

txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(3, 6):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          font=('arial', 16, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnDelete = Button(calc, width=6, height=2, text="DEL", font=('arial', 16, 'bold'), bd=4, bg="gray",
                   command=added_value.deleteBS).grid(row=1, column=0, pady=1)
btnClear = Button(calc, width=6, height=2, text="C", font=('arial', 16, 'bold'), bd=4, bg="gray",
                  command=added_value.All_Clear_Entry).grid(row=1, column=1, pady=1)
btnClearAll = Button(calc, width=6, height=2, text="CE", font=('arial', 16, 'bold'), bd=4, bg="gray",
                     command=added_value.Clear_Entry).grid(row=1, column=2, pady=1)
btnPlusMinus = Button(calc, width=6, height=2, text=chr(177), font=('arial', 16, 'bold'), bd=4, bg="gray",
                      command=added_value.Plus_Minus).grid(row=1, column=3, pady=1)

btnSqr = Button(calc, width=6, height=2, text="√", font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=added_value.squared).grid(row=2, column=0, pady=1)
btnCos = Button(calc, width=6, height=2, text="Cos", font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=added_value.cos).grid(row=2, column=1, pady=1)
btnTan = Button(calc, width=6, height=2, text="Tan", font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=added_value.tan).grid(row=2, column=2, pady=1)
btnSin = Button(calc, width=6, height=2, text="Sin", font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=added_value.sin).grid(row=2, column=3, pady=1)

btnPlus = Button(calc, width=6, height=2, text="+", font=('arial', 16, 'bold'), bd=4, bg="gray",
                 command=lambda: added_value.operation("plus")).grid(row=3, column=3, pady=1)
btnMinus = Button(calc, width=6, height=2, text="-", font=('arial', 16, 'bold'), bd=4, bg="gray",
                  command=lambda: added_value.operation("minus")).grid(row=4, column=3, pady=1)
btnTimes = Button(calc, width=6, height=2, text="x", font=('arial', 16, 'bold'), bd=4, bg="gray",
                  command=lambda: added_value.operation("times")).grid(row=5, column=3, pady=1)
btnDiv = Button(calc, width=6, height=2, text=chr(247), font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=lambda: added_value.operation("divide")).grid(row=6, column=3, pady=1)

btnZero = Button(calc, width=6, height=2, text="0", font=('arial', 16, 'bold'), bd=4, bg="gray",
                 command=added_value.numberEnter).grid(row=6, column=0, pady=1)
btnDot = Button(calc, width=6, height=2, text=".", font=('arial', 16, 'bold'), bd=4, bg="gray",
                command=added_value.numberEnter).grid(row=6, column=1, pady=1)
btnEqual = Button(calc, width=6, height=2, text="=", font=('arial', 16, 'bold'), bd=4, bg="gray",
                  command=added_value.sum_of_total).grid(row=6, column=2, pady=1)

main.mainloop()
