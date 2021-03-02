print("Enter the data : ")
x = []
temp = float(input())
while(temp!=-1):
    x.append(temp)
    temp = float(input())
min_x = min(x)
max_x = max(x)

print("\nNew min : " , end="")
new_min = float(input())
print("New max : " , end="")
new_max = float(input())

print("\nWant to Sort? (1/0) : ", end="")
t = int(input())
if(t==1):
    x.sort()

print("\n\nMin : " + str(min_x))
print("\n\nMax : " + str(max_x))
new_x = []
print("\n\nv\t\tv'")
for i in range(0, len(x)):
    temp = ( (x[i] - min_x) * (new_max - new_min) / (max_x - min_x) ) + new_min
    new_x.append(temp)
    print(str(x[i]) + "\t\t" + str(new_x[i]))
