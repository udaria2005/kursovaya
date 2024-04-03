from math import *
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
root = tk.Tk()
root.iconbitmap('gigachad.ico')
root.config(bg='#ffdcc3')
root.title('Интерполяционный многочлен Лагранжа и Python')
root.geometry('400x300+50+50')

label_1 =tk.Label(root, text = 'Введите координату x', 
                  bg = '#ffdcc3',
                  fg = 'brown',
                  font = ('Comic Sans MS',12),
                  )
label_1.grid()

countx=0
county=0
massivex = []
massivey = []

def add_label():
    label = tk.Label(root,text='dd')   
    label.pack()
    
def xdata():
    global massivex
    valuex = xent.get()
    if valuex:
        massivex.append(valuex)
    else:
        print('Срочно перезапустите программу!')
    global countx
    countx+=1 
    btn1['text'] = f'OK:{countx}'
    xent.delete(0,'end')
    

    
def ydata():
    global massivey
    valuey = yent.get()
    if valuey:
        massivey.append(valuey)
    else:
        print('Срочно перезапустите программу!')
    global county
    county+=1 
    btn2['text'] = f'OK:{county}'
    yent.delete(0,'end')
    
xent = tk.Entry(root)
xent.grid(row=1,column=0)

yent = tk.Entry(root)
yent.grid(row=4,column=0)
    
btn1 = tk.Button(root, text=f'OK: {countx}',
                 activebackground='light blue',
                 command=xdata)
btn1.grid(row=1,column=1)

label_2 =tk.Label(root, text = 'Введите координату y', 
                  bg = '#ffdcc3',
                  fg = 'brown',
                  font = ('Comic Sans MS',12),
                  )
label_2.grid(row=3,column=0)

btn2 = tk.Button(root, text=f'OK: {county}',
                 activebackground='light blue',
                 command=ydata)
btn2.grid(row=4,column=1)

def canvasmaker():
    if countx==county:        
        
        c=round(float(max(massivex)))
        v=float(min(massivex))
        e=(c-v)/4/countx
        z=[]
        y=[]
        for t in range (4*countx+1):
            x=float(min(massivex))
            x=x+e*t
            f=0
            for j in range (countx):
                p1=1
                p2=1 
                
                for i in range (countx):
                    if i!=j:
                        p1=p1*(x-float(massivex[i]))
                        p2=p2*(float(massivex[j])-float(massivex[i]))
                g=p1/p2
                f=f+float(massivey[j])*g
            z.append(x)
            y.append(f)
        b = [0]*len(z)
        a = np.sort(z)
        for i in range(0,len(z)):
            for j in range(0,len(z)):
                if a[j]==z[i]:
                    b[j]=y[i]
        plt.plot(a,b)
        plt.show()


btn3  = tk.Button(root, text='Построить график!',
                  activebackground='light blue',
                  command=canvasmaker)

btn3.grid(row = 5,column = 0, columnspan=2)



root.mainloop()