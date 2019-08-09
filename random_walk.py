from typing import List, Any

from numpy import *
import numpy as np
import math

def program():
    l = float(input("enter the value of lambda: "))
    N = int(input("enter the value of N: "))
    e = float(input("enter the value of e: "))           #input lambda, N and e
    X = []
    X.append(list([float(input("enter x: ")), float(input("enter y: "))]))
    X0 = X
    X1 = []
    index = 0       #initial solution X0

    while (l >= e):
        X1 = findNext(X0,l)                    #evaluate X1 for given X0 and l
        f0=funcValue(X0)
        f1=funcValue(X1)
        print("X0: ", X0,"\tf0: ",f0)
        print("X1: ", X1,"\tf1: ",f1)           #find values of f1 and f2

        if (f1 >= f0) or (abs(X1[0][0]) > 100.0) or (abs(X1[0][1]) > 100.0):
            index += 1
            if index > N:                       #after N unsuccessful trials, change step length
                l /= 2
                print("Lambda: ",l,"\n")
        else:
            X0 = X1                             #accept solution if successful
            index = 0

    print("optimal solution:", X0)


def findNext(T,l):
    r = []
    r=np.array([random.random() * random.choice((-1, 1)),random.random() * random.choice((-1, 1))])
    sq = math.sqrt(math.pow(r[0], 2) + math.pow(r[1], 2))
    u = r/sq                                     #finding direction parameter u
    X1=T+(u*l)
    return X1

def funcValue(T):
    return 4*pow(T[0][0],2)+pow(T[0][1],2)-(3*T[0][0]*T[0][1])+(6*T[0][0])+(12*T[0][1]) #evaluate polynomial function