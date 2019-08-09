import numpy as np
from numpy import *
import math



def program():
    n = int(input("enter the value of n: "))
    xmin = float(input("input min value: "))
    xmax = float(input("input max value: "))

    dx = float((xmax - xmin) / n)
    x1 = xmin
    x2 = xmin + dx
    c = 0
    for i in range(n-2):
        x3=x2+dx
        print(x1,x2,x3)
        f1=func(x1)
        f2=func(x2)
        f3=func(x3)
        print(f1,f2,f3)

        if f1>=f2<=f3:
            c=1
            break
        x1=x2
        x2=x3
    if c is 1:
        print("minima lies in the range: (%f,%f)"%(x1,x3))
    else:
        print("no minima found")


def func(x):
    return (32/(x*x))+x


