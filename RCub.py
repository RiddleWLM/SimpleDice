from tkinter import *
from PIL import Image 
import random

root = Tk()

x = round(random.uniform(1, 6))

print(x)

if x==1:
    img=PhotoImage(file='cub1.png')
if x==2:
    img=PhotoImage(file='cub2.png')
if x==3:
    img=PhotoImage(file='cub3.png')
if x==4:
    img=PhotoImage(file='cub4.png')
if x==5:
    img=PhotoImage(file='cub5.png')
if x==6:
    img=PhotoImage(file='cub6.png')

l = Label(root, image=img)

l.pack()

root.geometry()
root.mainloop()