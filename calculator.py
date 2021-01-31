import tkinter as tk, tkinter.font as tkf
import decimal
from math import *

#thanks to aditya agarwal for the lambda functon wizardry

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
wide, high = 6, 3
expression = ''

'''this function defines the write function for calculation in the calculator'''
def buildExpression(char):
    global expression
    if(len(expression) > 0):
        if(char=='.' and not expression[-1].isdigit()): return None
        if(not char.isdigit() and expression[-1] == '.'): return None
        if(char.isdigit() and expression[-1] == ')'): return None
        if(char == '(' and expression[-1].isdigit()): return None
        
    expression += char
    output.configure (text = expression)

'''this function resets the writespace'''
def clearExpression():
    global expression
    expression = ""
    output.config(text = 'All Cleared!')

'''this function deletes the last character entered into the writespace'''
def delExpression():
    global expression
    expression = expression[:len(expression)-1]
    if(expression[-1] == '.'): expression = expression[:len(expression)-1]
    output.config(text = expression)

'''debug function'''
def execute():
    global expression
    try:
        expression = str(eval(expression))
    except:
        output.config(text = 'Syntax Error!')
        return None
    
    expression = expression.split('.')
    if(len(expression) == 1 or int(expression[1])==0): expression = expression[0]
    else : expression = expression[0] + '.' + expression[1]
    
    output.configure (text = expression)

'''this function is to make it easier for creating the GUI interface by automating the creation of buttons'''  
def getButton(char, callback):
    return tk.Button(root, width=wide, height=high, text=char, command=callback)

#window
root  = tk.Tk()
root.geometry('370x275')
root.title('Calculator') 

numberButtons = [(lambda num : tk.Button(root, text = num, command = lambda: buildExpression(num), height = high, width = wide, bg = '#aeaeae'))(str(i)) for i in range(0, 10)]

# Simple arithmetic functions
buttonEqual = getButton('=', execute)
buttonPlus = getButton('+', lambda : buildExpression('+'))
buttonMinus = getButton('-', lambda : buildExpression('-'))
buttonProd = getButton('*', lambda : buildExpression('*'))
buttonDiv = getButton('/', lambda : buildExpression('/'))
buttonPow = getButton('^', lambda : buildExpression('**'))
buttonDec = getButton('.', lambda : buildExpression('.'))
buttonPerCent = getButton('%', lambda : buildExpression('*0.01'))
buttonLBrack = getButton('(', lambda: buildExpression('(') )
buttonRBrack = getButton(')', lambda: buildExpression(')') )


# -- TODO --
#log
#radians->degrees
#trig functions

buttonSin = getButton('sin', lambda : buildExpression('sin'))
buttonCos = getButton('cos', lambda : buildExpression('cos'))
buttonTan = getButton('tan', lambda : buildExpression('tan'))
buttonSec = getButton('sec', lambda : buildExpression('1/cos'))
buttonCosec = getButton('csc', lambda : buildExpression('1/sin'))
buttonCot = getButton('cot', lambda : buildExpression('1/tan'))


#bitwise Functions
'''
buttonNot = getButton('not', lambda : sign('+'))
buttonAnd = getButton('and', lambda : sign('+'))
buttonOr = getButton('or', lambda : sign('+'))
buttonXor = getButton('xor', lambda : sign('+'))
'''


buttonDelete = getButton('CE', delExpression)
buttonReset = getButton('AC', clearExpression)

for i in range(1, 10): numberButtons[i].grid(row = int((i+2)//3), column = 1+((i-1)%3))
numberButtons[0].grid(row = 4, column = 2)

buttonPlus.grid(row = 1, column = 4)
buttonPow.grid(row = 1, column = 5)

buttonMinus.grid(row = 2, column = 4)
buttonPerCent.grid(row = 2, column = 5)

buttonProd.grid(row = 3, column = 4)
buttonDelete.grid(row = 3, column = 5)

buttonDec.grid(row = 4, column = 1)
buttonEqual.grid(row = 4, column = 3)
buttonDiv.grid(row = 4, column = 4)
buttonReset.grid(row = 4, column = 5)
buttonLBrack.grid(row = 4, column = 6)
buttonRBrack.grid(row = 4, column = 7)


buttonSin.grid(row = 1, column = 6)
buttonCos.grid(row = 2, column = 6)
buttonTan.grid(row = 3, column = 6)

buttonSec.grid(row = 1, column = 7)
buttonCosec.grid(row = 2, column = 7)
buttonCot.grid(row = 3, column = 7)

output = tk.Label(root, text='Enter your expression:' , bg = '#c9c9c9', width = 49, height = 3, relief = 'sunken', anchor = 'w', padx = 10, font=('Calibri', 10, 'bold'))
output.grid(row = 5, column = 1, columnspan = 7, rowspan = 25)

root.mainloop()
