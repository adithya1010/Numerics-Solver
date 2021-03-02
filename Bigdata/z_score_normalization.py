import numpy as np
print("Enter the data : ")
x = []
temp = float(input())
while(temp!=-1):
    x.append(temp)
    temp = float(input())

print("\nWant to Sort? (1/0) : ", end="")
if(int(input())==1):
    x.sort()

mean_x = np.mean(x)
std_x = np.std(x)

new_x = []

print("\n\nMean : " + str(mean_x))
print("Standard Deviation : " + str(std_x))
print("\n\nx\t\tx'")
for i in range(0, len(x)):
    temp = (x[i] - mean_x) / std_x
    new_x.append(temp)
    print(str(x[i]) + "\t\t" + str(new_x[i]))
