from re import X
from tkinter import Y


x = 10
y = 10
x = ++x + ++x + --x
y = --y - --y - ++y
z = ++x - --y
print(x,y,z)
