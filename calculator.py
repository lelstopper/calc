
#import
import tkinter as tk
import tkinter.font as tkf

# ! TODO
#debug related stuff
DBG = 0 # 0 - nothing, 1 - something, 2 - detailed
if(DBG==0): print1 = lambda *args, **kwargs : print(*args, **kwargs)
elif(DBG==1): print2 = lambda *args, **kwargs : print(*args, **kwargs)
elif(DBG==2): print3 = lambda *args, **kwargs : print(*args, **kwargs)

#fns & vars
x = ''
a = 0
b = 0
sign1 = ''
wide = 6
high = 3
signs = ['+', '-']

def quitapp():
    root.destroy()

def press(num):
    global x
    
    x += str(num)
    print(x)

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
    
    if x.find('.') == -1:
        b = int(x)

    else:
        b = float(x)
    
    dict1 = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b, '%': b / 100}
    for i in dict1:
        if i == sign1:
            print('= ' + str(dict1[i]))
            x = str(dict1[i])
    
#window
root  = tk.Tk()
root.geometry('400x400')
root.title('calculator') 

#buttons
QuitButton = tk.Button(
                    root,
                    text = 'Quit',
                    command = quitapp,
                    justify = 'center',
                    width = wide,
                    height = high
                    )

'''col = 1

listNumbers = [1,1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    b = tk.Button(root,
                  text = str(i),
                  command = lambda: press(int(b.cget('text'))),
                  width = wide,
                  height = high,
                  )
    
    b.grid(row = ((i-1) % 3)+ 1, column = col)
    if i % 3 == 0:
        col += 1'''


button1 = tk.Button(root,
                text='1',
                command = lambda: press(1),
                height = high,
                width = wide) 

button2 = tk.Button(root,
                text='2',
                command = lambda: press(2),
                height = high,
                width = wide) 
button3 = tk.Button(root,
                text='3',
                command = lambda: press(3),
                height = high,
                width = wide) 
    
button4 = tk.Button(root,
                text='4',
                command = lambda: press(4),
                height = high,
                width = wide) 
    
button5 = tk.Button(root,
                text='5',
                command = lambda: press(5),
                height = high,
                width = wide) 
    
button6 = tk.Button(root,
                text='6',
                command = lambda: press(6),
                height = high,
                width = wide) 
    
button7 = tk.Button(root,
                text='7',
                command = lambda: press(7),
                height = high,
                width = wide) 
    
button8 = tk.Button(root,
                text='8',
                command = lambda: press(8),
                height = high,
                width = wide) 
    
button9 = tk.Button(root,
                text='9',
                command = lambda: press(9),
                height = high,
                width = wide)
    

buttonEqual = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '=',
                    command = equal
                    )

buttonPlus = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '+',
                    command = lambda: sign('+')
                    )

buttonMinus = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '-',
                    command = lambda: sign('-')
                    )

buttonProd = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '*',
                    command = lambda: sign('*')
                    )
buttonDiv = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '/',
                    command = lambda: sign('/')
                    )

buttonPow = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '^',
                    command = lambda: sign('^')
                    )

buttonDec = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '.',
                    command = point
                    )

buttonPerCent = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '%',
                    command = percent
                    )
#log
#trig functions

buttonDelete = tk.Button(root,
                    width = wide,
                    height = high,
                    text = 'CE',
                    command = delete
                    )

button0 = tk.Button(root,
                    width = wide,
                    height = high,
                    text = '0',
                    command = lambda: press(0)
                    )

buttonReset = tk.Button(root,
                    width = wide,
                    height = high,
                    text = 'X',
                    command = reset
                    )


                    
button0.grid(row = 4, column = 2)
button1.grid(row = 1, column = 1)
button2.grid(row = 1, column = 2)
button3.grid(row = 1, column = 3)
button4.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)
button6.grid(row = 2, column = 3)
button7.grid(row = 3, column = 1)
button8.grid(row = 3, column = 2)
button9.grid(row = 3, column = 3)

buttonEqual.grid(row = 4, column = 3)
buttonPlus.grid(row = 1, column = 4)
buttonMinus.grid(row = 2, column = 4)
buttonProd.grid(row = 3, column = 4)
buttonDiv.grid(row = 4, column = 4)
buttonPow.grid(row = 1, column = 5)
buttonDec.grid(row = 3, column = 5)
buttonPerCent.grid(row = 2, column = 5)

buttonReset.grid(row = 4, column = 5)
buttonDelete.grid(row = 6 , column = 5)
QuitButton.grid(row = 4, column = 1)

root.mainloop()
