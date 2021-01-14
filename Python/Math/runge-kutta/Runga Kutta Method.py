import math as m
import csv

h = .0001
y0 = 0
t0 = 0
tf = 10

def f(t,y):
#    return -2*y+2-m.exp(-4*t)
    return y - m.exp(t/2)*m.sin(5*t)/2 + 5*m.exp(t/2)*m.cos(5*t)
yn = y0
tn = t0

output = [[tn,yn]]
for i in range(int(tf/h)):
    k1 = h*f(tn,yn)
    k2 = h*f(tn+h/2,yn+k1/2)
    k3 = h*f(tn+h/2,yn+k2/2)
    k4 = h*f(tn+h,yn+k3)
#    k1 = h*f(tn,yn)
#    k2 = h*f(tn+.4*h,yn+.4*k1)
#    k3 = h*f(tn+.45573725*h,yn+.29697761*k1+.15875964*k2)
#    k4 = h*f(tn+h,yn+.21810040*k1-3.05096516*k2+3.83286476*k3)
    tn = tn + h
    yn = yn + (k1 + 2*k2 + 2*k3 + k4)/6.
#    yn = yn + .17476028*k1-.55148066*k2+1.20553560*k3+.17118478*k4
    output.append([tn,yn])

with open('output.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output)
