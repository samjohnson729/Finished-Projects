import random

data = {}
num = 100
for i in range(num):
    data[i] = (i-20)*(i-10)*(2*i-50) * (1 + random.randrange(-1,2)*random.random()*.01)

#Define SCORING function
def score(data,a,b,c,d):
    for key in data.keys():
        total = ((a + b*key + c*key**2 + d*key**3) - data[key])**2
    return total**(.5)/len(data)

#Useful Statistics
Sx = float(sum(data.keys()))/len(data)
Sy = float(sum(data.values()))/len(data)
Sxx = 0.
Syy = 0.
Sxy = 0.
Sxxy = 0.
Sxxx = 0.
Sxxxy = 0.
Sxxxx = 0.
Sxxxxx = 0.
Sxxxxxx = 0.
for key in data.keys():
    Sxx = Sxx + key**2
    Syy = Syy + data[key]**2
    Sxy = Sxy + key*data[key]
    Sxxy = Sxxy + key**2*data[key]
    Sxxx = Sxxx + key**3
    Sxxxy = Sxxxy + key**3*data[key]
    Sxxxx = Sxxxx + key**4
    Sxxxxx = Sxxxxx + key**5
    Sxxxxxx = Sxxxxxx + key**6
Sxx = Sxx/len(data)
Syy = Syy/len(data)
Sxy = Sxy/len(data)
Sxxy = Sxxy/len(data)
Sxxx = Sxxx/len(data)
Sxxxy = Sxxxy/len(data)
Sxxxx = Sxxxx/len(data)
Sxxxxx = Sxxxxx/len(data)
Sxxxxxx = Sxxxxxx/len(data)
sigmaxx = Sxx - Sx*Sx
sigmax2x = Sxxx - Sxx*Sx
sigmax2x2 = Sxxxx - Sxx*Sxx
sigmaxy = Sxy - Sx*Sy
sigmax2y = Sxxy - Sxx*Sy
sigmax3x = Sxxxx - Sxxx*Sx
sigmax3y = Sxxxy - Sxxx*Sy
sigmax3x2 = Sxxxxx - Sxxx*Sxx
sigmax3x3 = Sxxxxxx - Sxxx*Sxxx

#Constant Guessing
b = 0
c = 0
d = 0
a = float(sum(data.values()))/len(data.values())
print score(data,a,b,c,d)

#Linear Guessing
c = 0
d = 0
b = (Sxy - Sx*Sy)/(Sxx - Sx*Sx)
a = (Sy - b*Sx)
print score(data,a,b,c,d)

#Quadratic Guessing
d = 0
c = (sigmax2y*sigmaxx - sigmax2x*sigmaxy)/(sigmaxx*sigmax2x2 - sigmax2x*sigmax2x)
b = (sigmaxy - c*sigmax2x)/sigmaxx
a = Sy - b*Sx - c*Sxx
print score(data,a,b,c,d)

#Cubic Guessing
d = ( (sigmax3y*sigmaxx-sigmax3x*sigmaxy)*(sigmax2x2*sigmaxx-sigmax2x*sigmax2x) - (sigmaxx*sigmax2y-sigmax2x*sigmaxy)*(sigmax3x2*sigmaxx-sigmax3x*sigmax2x) ) / ( (sigmax3x3*sigmaxx-sigmax3x*sigmax3x)*(sigmax2x2*sigmaxx-sigmax2x*sigmax2x) - (sigmax3x2*sigmaxx-sigmax2x*sigmax3x)*(sigmax3x2*sigmaxx-sigmax3x*sigmax2x) )
c = ( (sigmaxx*sigmax2y-sigmax2x*sigmaxy) - d*(sigmax3x2*sigmaxx-sigmax2x*sigmax3x) ) / (sigmax2x2*sigmaxx-sigmax2x*sigmax2x)
b = (sigmaxy - c*sigmax2x - d*sigmax3x)/sigmaxx
a = Sy-b*Sx-c*Sxx-d*Sxxx
print score(data,a,b,c,d)
print "a: ",a,"\nb: ",b,"\nc: ",c,"\nd: ",d
