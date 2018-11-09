import matplotlib.pyplot as plt
import csv
x = []
y = []
z = []
u = []
with open('lab.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        #x.append(float(row[0]))
        #y.append(float(row[1]))
        z.append(float(row[2]))
        u.append(float(row[3]))
#plt.plot(x,y, label='Forward Bias', color='orange')
plt.plot(z,u, label='reverse Bias', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()