import numpy as np

print("Enter -1 to finish the data entry\nEnter the data :")
x=[]
temp = np.float16(input())
while(temp!=-1):
    x.append(temp)
    temp = float(input())
print("\n")
mean_x=np.mean(x)
median_x=np.median(x)

x.sort()    
q1 = np.quantile(x,.25)
q3 = np.quantile(x,.75)
iqr = q3 - q1
print("Sorted Data :")
print(x)
print("Mean   : " + str(mean_x))
print("Median : " + str(median_x))
print("Q1     : " + str(q1))
print("Q3     : " + str(q3))
print("\n")

print("Low\tQ1\tMedian\tQ3\tHigh")
print(str(min(x)) +"\t"+ str(q1) + "\t" + str(median_x) + "\t" + str(q3) + "\t" + str(max(x)))

print("\n\nInterQuartile Range : " + str(q1) + " to " + str(q3) + " | -> | " + str(iqr))

outlow  = q1 - (1.5*iqr)
outhigh = q3 + (1.5*iqr)
print("\n\nOutliers :")
print("Below " + str(outlow) + " and above " + str(outhigh))
for i in x:
    if(i<outlow or i>outhigh):
        print(i, end=" ")
print("\n")

