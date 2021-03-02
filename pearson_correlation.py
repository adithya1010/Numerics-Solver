import numpy as np
import math

from numpy.core.fromnumeric import var
print("Pearson Correlation (r)\nEnter the x values :")
x = []
temp = float(input())
while(temp!=-1):
    x.append(temp)
    temp = float(input())

print("\nEnter the y values :")
y = []
temp = float(input())
while(temp!=-1):
    y.append(temp)
    temp = float(input())

mean_x = np.mean(x)
mean_y = np.mean(y)
print("Mean of x : " + str(round(mean_x,2)))
print("Mean of y : " + str(round(mean_y,2)))

variance = []
variancex = []
variancey = []
print("\nXi-Mean(x)\tYi-Mean(y)\tProduct")
for i in range(0, len(x)):
    variance.append((x[i]-mean_x)*(y[i]-mean_y))
    print(str(round((x[i]-mean_x),2)) + "\t\t" + str(round((y[i]-mean_y),2)) + "\t\t" + str(round(variance[i],2)))
    variancex.append((x[i]-mean_x)*(x[i]-mean_x))
    variancey.append((y[i]-mean_y)*(y[i]-mean_y))
print("\t\t\t\t-----")
print("\t\t\t\t" + str(round(sum(variance),2)))

print("\n(Xi-Mean(x))^2\tYi-Mean(y))^2")
for i in range(0, len(x)):
    print(str(round(variancex[i],2)) + "\t\t" + str(round(variancey[i],2)))
print("-----\t\t-----\t\tProduct")
print(str(round(sum(variancex),2)) + "\t\t" + str(round(sum(variancey),2)) + "\t\t" + str(round(sum(variancex)*sum(variancey),2)))
print("\t\t\t\tRoot()")
print("\t\t\t\t" + str(round(math.sqrt(sum(variancex)*sum(variancey)),2)))

num = sum(variance)
denom = math.sqrt(sum(variancex)*sum(variancey))
pc = num / denom
print("\n\nPerson Coefficient : " + str(pc))
