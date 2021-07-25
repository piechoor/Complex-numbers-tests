from complex_num import *
from tkinter import *

CONST_FG = '#2cc72c' # FOREGROUND COLOR
CONST_BG = 'black' # BACKGROUND COLOR

root = Tk()
root.configure(bg=CONST_BG)
root.title('Complex numbers calculator')
root.geometry('240x200')

### LABELS BEYOND CELLS ###
xNumberLab = Label(root, text='x number:', fg=CONST_FG, bg=CONST_BG)
yNumberLab = Label(root, text='y number:', fg=CONST_FG, bg=CONST_BG)
zNumberLab = Label(root, text='z number:', fg=CONST_FG, bg=CONST_BG)
entryLab = Label(root, text='rownanie:', fg=CONST_FG, bg=CONST_BG)
formatLab = Label(root, text='postac /a/t/e/:', fg=CONST_FG, bg=CONST_BG)
buttonLab = Label(root, text=' ', fg=CONST_FG, bg=CONST_BG)

xNumberLab.grid(row=0, column=0)
yNumberLab.grid(row=0, column=1)
zNumberLab.grid(row=0, column=2)
entryLab.grid(row=2, column=0)
formatLab.grid(row=2, column=1)
buttonLab.grid(row=2, column=2)
############################

### ENTRY CELLS ###
xNumIn = Entry(root, width=12, borderwidth=1, fg='white', bg=CONST_BG, justify='center')
yNumIn = Entry(root, width=12, borderwidth=1, fg='white', bg=CONST_BG, justify='center')
zNumIn = Entry(root, width=12, borderwidth=1, fg='white', bg=CONST_BG, justify='center')
eqIn = Entry(root, width=12, borderwidth=1, fg='white', bg=CONST_BG, justify='center')
formIn = Entry(root, width=12, borderwidth=1, fg='white', bg=CONST_BG, justify='center')

xNumIn.grid(row=1, column=0)
yNumIn.grid(row=1, column=1)
zNumIn.grid(row=1, column=2)
eqIn.grid(row=3, column=0)
formIn.grid(row=3, column=1)
#####################

### SOLUTION CELL ###
solLab = Label(root, fg=CONST_FG, bg=CONST_BG)
solLab.grid(row=4, columnspan=3)
#####################

### CLEANING ENTRY CELLS ###
def cleanIn():
    xNumIn.delete(0,100)
    yNumIn.delete(0,100)
    zNumIn.delete(0,100)
    eqIn.delete(0,100)
    formIn.delete(0,100)
#############################

### SHOWING SOLUTION IN A GIVEN FORMAT ###
def ShowInForm(form, solution):
    if form =='a':
        solLab.configure(text=solution)
    elif form == 't':
        arg = solution.argument()
        r = solution.modulus()
        solLab.configure(text="{}(cos({})+isin({}))".format(r, arg, arg))
    elif form == 'e':
        solLab.configure(text="e^({}i)".format(solution.argument()))
    else:
        solLab.configure(text="Wrong format.")
###########################################

### ANALYZE NUMBER ###
def analNum(input):
    if input == '' or input == '0':
        return Complex(0, 0)
    elif input.find('+') == -1: #NO PLUS SIGN
        data = input.strip('i')
        lst = data.split('-')
        return Complex(int(lst[0]), -int(lst[1]))
    elif input.find('-') == -1: #NO MINUS SIGN
        data = input.strip('i')
        lst = data.split('+')
        return Complex(int(lst[0]), int(lst[1]))

### SOLVE EQUATION ###
def solveEq():
    x = analNum(xNumIn.get())
    y = analNum(yNumIn.get())
    z = analNum(zNumIn.get())

    equation = eqIn.get()
    form = formIn.get()

    Solution = eval(equation)
    ShowInForm(form, Solution)


solveButton = Button(root, command=solveEq, padx=15, text='OBLICZ', fg=CONST_FG, bg=CONST_BG)
solveButton.grid(row=3,column=2)
####################

root.mainloop()