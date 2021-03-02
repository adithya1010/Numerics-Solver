import numpy as np
import math

print("Enter the X data : ")
x = []
temp = float(input())
while(temp!=-1):
    x.append(temp)
    temp = float(input())

print("\nEnter the Y data : ")
y = []
temp = float(input())
while(temp!=-1):
    y.append(temp)
    temp = float(input())

print("\nValue of x : ", end="")
new_x = float(input())

mean_x = np.mean(x)
mean_y = np.mean(y)
print("\n\nMean(x) : " + str(mean_x))
print("\n\nMean(y) : " + str(mean_y))

num = 0
print("\n\nXi-Mean(x)\tYi-Mean(Y)\tProduct")
for i in range(0, len(x)):
    print(str(round((x[i]-mean_x),2)) + "\t\t" + str(round((y[i]-mean_y),2)) + "\t\t" + str(round((x[i]-mean_x)*(y[i]-mean_y),2)))
    num = num + (x[i]-mean_x) * (y[i]-mean_y)
print("\t\t\t\t-----")
print("\t\t\t\t" + str(round(num,2)))

denum = 0
print("\n\nX1-Mean(X)^2")
for i in range(0, len(x)):
    print(round(math.pow((x[i]-mean_x),2),2))
    denum = denum + math.pow((x[i]-mean_x),2)
print("-----")
print(denum)

w1 = num/denum
w0 = mean_y - (w1*mean_x)
print("\n\nw1 = " + str(round(w1,2)))
print("\n\nw2 = " + str(round(w0,2)))

new_y = w0 + (w1 * new_x)

print("\n\nThe value of y : " + str(round(new_y,2)))
