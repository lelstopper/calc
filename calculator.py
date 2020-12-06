
#import
import tkinter as tk
import tkinter.font as tkf

# ! TODO
#debug related stuff
DBG = 1 # 0 - nothing, 1 - something, 2 - detailed
print1 = lambda *args, **kwargs : None
print2 = lambda *args, **kwargs : None
print3 = lambda *args, **kwargs : None
if(DBG==1): print1 = lambda *args, **kwargs : print(*args, **kwargs)
elif(DBG==2): print2 = lambda *args, **kwargs : print(*args, **kwargs)
elif(DBG==3): print3 = lambda *args, **kwargs : print(*args, **kwargs)

#fns & vars
x, sign1, a, b = '', '',  0, 0
wide, high = 6, 3
signs = ['+', '-']
expression = ''

def buildExpression(char):
    expression += char

def press(num):
    global x
    
    x += str(num)
    print1(x)

def point():
    global x
    x += '.'

def sign(sign):
    global x, sign1, a

    a = int(x) if(x.find('.') == -1) else float(x)
        
    x = ''
    sign1 = sign
    print1(sign)

def percent():
    global x, sign1
    y = ''
    sign1 = '%'

    b = int(x) if(x.find('.') == -1) else float(x)
    
    y = x + '%'
    print1(y)
    
def delete():
    global x
    listx = (list(x))[:-1]
    x = ''.join(listx)
    
    print1(x)

def reset():
    global x, a, b, sign1
    x = ''
    a = 0
    b = 0
    sign1 = ''
    print('the calculator has been reset.')

def equal():
    global sign1, x, a, b

    b = int(x) if(x.find('.') == -1) else float(x)
    
    dict1 = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b, '%': b / 100}
    for i in dict1:
        if i == sign1:
            print('= ' + str(dict1[i]))
            x = str(dict1[i])
    
#window
root  = tk.Tk()
root.geometry('400x400')
root.title('calculator') 

numberButtons = [(lambda num : tk.Button(root, text = str(num), command = lambda: press(num), height = high, width = wide ))(i) for i in range(0, 10)]

def getButton(char, callback):
    return tk.Button(root, width=wide, height=high, text=char, command=callback)

# Simple arithmetic functions
buttonEqual = getButton('=', equal)
buttonPlus = getButton('+', lambda : sign('+'))
buttonMinus = getButton('-', lambda : sign('-'))
buttonProd = getButton('*', lambda : sign('*'))
buttonDiv = getButton('/', lambda : sign('/'))
buttonPow = getButton('^', lambda : sign('^'))
buttonDec = getButton('.', lambda : point)
buttonPerCent = getButton('%', lambda : percent)

#! TODO
#log
#trig functions
'''
buttonPlus = getButton('sin', lambda : sign('+'))
buttonPlus = getButton('cos', lambda : sign('+'))
buttonPlus = getButton('tan', lambda : sign('+'))
buttonPlus = getButton('sec', lambda : sign('+'))
buttonPlus = getButton('csec', lambda : sign('+'))
buttonPlus = getButton('cot', lambda : sign('+'))
'''
#bitwise Functions
'''
buttonPlus = getButton('not', lambda : sign('+'))
buttonPlus = getButton('and', lambda : sign('+'))
buttonPlus = getButton('or', lambda : sign('+'))
buttonPlus = getButton('xor', lambda : sign('+'))
'''

buttonDelete = getButton('CE', delete)
buttonReset = getButton('AC', reset)

for i in range(1, 10): numberButtons[i].grid(row = int((i+2)//3), column = 1+((i-1)%3))
numberButtons[0].grid(row = 4, column = 2)

buttonEqual.grid(row = 4, column = 3)
buttonPlus.grid(row = 1, column = 4)
buttonMinus.grid(row = 2, column = 4)
buttonProd.grid(row = 3, column = 4)
buttonDiv.grid(row = 4, column = 4)
buttonPow.grid(row = 1, column = 5)
buttonDec.grid(row = 3, column = 5)
buttonPerCent.grid(row = 2, column = 5)
buttonReset.grid(row = 4, column = 5)
buttonDelete.grid(row = 4, column = 1)

root.mainloop()
