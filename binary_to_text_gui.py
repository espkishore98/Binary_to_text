# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:10:57 2020

@author: Om
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:27:17 2020

@author: Om
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:39:59 2020

@author: Om
"""
import tkinter as tk
from tkinter import messagebox as mb

def get_decimals():
    number=[]
    numbers=text.get()
    li = list(numbers.split(" "))
    for give in li:
        number.append(int(give,2))
    
    return number
    
        
def get_text():
    
    num=[]
    int_list=get_decimals()
    for i in int_list:
        
        x=chr(i)
        num.append(x)
        
    print(num)
    mb.showinfo("binary code is",num)
    return num



        
    
        
           

        
           
           



root=tk.Tk()
L1=tk.Label(root,text="Binary")
b1=tk.Button(root , text="submit", font = 30, width = 10, command=get_text)

text= tk.Entry(root)
L1.grid(row=0,column=0)
text.grid(row=0,column=1)
b1.grid(row=1,column=1)

root.mainloop()


