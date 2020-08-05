from tkinter import *
from PIL import Image 
import random

root = Tk()

x = round(random.uniform(1, 6))

print(x)

try:
    img=PhotoImage(file='cub' + str(x) + '.png')
except:
    print('Not found' + ' ' + x)

l = Label(image=img)
l.pack()

root.mainloop()