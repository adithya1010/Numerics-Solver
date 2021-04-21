import matplotlib.pyplot as plt

k = int(input("k : "))
n = []
for i in range(0, k):
    t = []
    temp1 = (float(input("Point " + str(i+1) + " :\nx :")))
    temp2 = (float(input("y :")))
    t.append(temp1)
    t.append(temp2)
    n.append(t)

temp1 = (float(input("\nC1  :\nx :")))
temp2 = (float(input("y :")))
c1 = [temp1, temp2]
temp1 = (float(input("\nC2  :\nx :")))
temp2 = (float(input("y :")))
c2 = [temp1, temp2]
temp1 = (float(input("\nC3  :\nx :")))
temp2 = (float(input("y :")))
c3 = [temp1, temp2]


c = []
print("\n\nS.No\tx\ty\tC1\tC2\tC3\tCluster\tNew Cluster Values :")
for i in range(0,k):
    t1 = ((((n[i][0] - c1[0] )**2) + ((n[i][1] - c1[1])**2) )**0.5)
    t2 = ((((n[i][0] - c2[0] )**2) + ((n[i][1] - c2[1])**2) )**0.5)
    t3 = ((((n[i][0] - c3[0] )**2) + ((n[i][1] - c3[1])**2) )**0.5)
    if(t1<=t2 and t1<=t3):
        c.append("C1")
        c1[0] = (c1[0] + n[i][0]) / 2
        c1[1] = (c1[1] + n[i][1]) / 2
        print(str(i+1) + "\t" + str(n[i][0]) + "\t" + str(n[i][1]) + "\t" + str(round(t1,4)) + "\t" + str(round(t2,4)) + "\t" + str(c[i]) + "\t(" + str(c1[0]) + "," + str(c1[1])+ ")")
        plt.scatter(n[i][0], n[i][1], c='coral')

    elif(t2<=t1 and t2<=t3):
        c.append("C2")
        c2[0] = (c2[0] + n[i][0]) / 2
        c2[1] = (c2[1] + n[i][1]) / 2
        print(str(i+1) + "\t" + str(n[i][0]) + "\t" + str(n[i][1]) + "\t" + str(round(t1,4)) + "\t" + str(round(t2,4)) + "\t" + str(c[i]) + "\t(" + str(c2[0]) + "," + str(c2[1]) + ")")
        plt.scatter(n[i][0], n[i][1], c='lightblue')
        
    elif(t3<=t1 and t3<=t2):
        c.append("C3")
        c3[0] = (c3[0] + n[i][0]) / 2
        c3[1] = (c3[1] + n[i][1]) / 2
        print(str(i+1) + "\t" + str(n[i][0]) + "\t" + str(n[i][1]) + "\t" + str(round(t1,4)) + "\t" + str(round(t2,4)) + "\t" + str(c[i]) + "\t(" + str(c3[0]) + "," + str(c3[1]) + ")")
        plt.scatter(n[i][0], n[i][1], c='black')

plt.title('K Means with 3 Clusters | Republic of Coders')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('K_Means_3_ROC.png')
plt.show()
