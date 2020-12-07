import tkinter as tk, tkinter.font as tkf
import decimal

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

def buildExpression(char):
    global expression
    if(len(expression) > 0):
        if(char=='.' and not expression[-1].isdigit()): return None
        if(not char.isdigit() and expression[-1] == '.'): return None
        if(char.isdigit() and expression[-1] == ')'): return None
        if(char == '(' and expression[-1].isdigit()): return None
    expression += char
    print(expression)

def clearExpression():
    global expression
    expression = ""
    print("All Cleared!")

def delExpression():
    global expression
    expression = expression[:len(expression)-1]
    if(expression[-1] == '.'): expression = expression[:len(expression)-1]
    print(expression)

def execute():
    global expression
    try:
        expression = str(eval(expression))
    except:
        print("Syntax Error!")
        return None
    expression = expression.split('.')
    if(len(expression) == 1 or int(expression[1])==0): expression = expression[0]
    else : expression = expression[0] + '.' + expression[1]
    print(expression)

def getButton(char, callback):
    return tk.Button(root, width=wide, height=high, text=char, command=callback)

#window
root  = tk.Tk()
root.geometry('400x400')
root.title('calculator') 

numberButtons = [(lambda num : tk.Button(root, text = num, command = lambda: buildExpression(num), height = high, width = wide ))(str(i)) for i in range(0, 10)]

# Simple arithmetic functions
buttonEqual = getButton('=', execute)
buttonPlus = getButton('+', lambda : buildExpression('+'))
buttonMinus = getButton('-', lambda : buildExpression('-'))
buttonProd = getButton('*', lambda : buildExpression('*'))
buttonDiv = getButton('/', lambda : buildExpression('/'))
buttonPow = getButton('^', lambda : buildExpression('**'))
buttonDec = getButton('.', lambda : buildExpression('.'))
buttonPerCent = getButton('%', lambda : buildExpression('*0.01'))

#! TODO
#log
#trig functions
'''
buttonSin = getButton('sin', lambda : sign('+'))
buttonCos = getButton('cos', lambda : sign('+'))
buttonTan = getButton('tan', lambda : sign('+'))
buttonSec = getButton('sec', lambda : sign('+'))
buttonCosec = getButton('csec', lambda : sign('+'))
buttonCot = getButton('cot', lambda : sign('+'))
'''
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
