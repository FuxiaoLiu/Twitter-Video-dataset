import matplotlib.pyplot as plt

'''
x = [4, 6, 8, 10,12,15,18,20,22]


k1 = [6, 10, 16, 22, 29, 37, 44, 53, 63, 69]
k2 = [6, 13, 25, 28, 45, 48, 53, 69, 84, 93]

#Ways to calculate the growth rate
tmp_k1 = []
for i in range(len(k1)):
    if i == len(k1)-1:
        break
    tmp1 = k1[i]
    tmp2 = k1[i+1]
    try:
        d = (tmp2-tmp1)/tmp1
    except:
        d = 0
    tmp_k1.append(d)

tmp_k2 = []
for i in range(len(k2)):
    if i == len(k2)-1:
        break
    tmp1 = k2[i]
    tmp2 = k2[i+1]
    try:
        d = (tmp2 - tmp1) / tmp1
    except:
        d = 0
    tmp_k2.append(d)
print(len(tmp_k1))
print(len(tmp_k2))


plt.plot(x,tmp_k1,'s-',color = 'r',label="Pyhop")
plt.plot(x,tmp_k2,'o-',color = 'g',label="Metric-FF")
plt.xlabel("Number of Blocks")
plt.ylabel("Growth Rate of Plan Length")
plt.legend(loc = "best")
plt.show()

'''
x = [1,2,3,4,5,6,7,8,9,10]

k1 = [13, 14.4, 13, 15, 13, 16, 14, 15, 15, 13, 10]
k2 = [9, 12, 13, 13, 13, 13, 15, 14, 12, 16, 12]

tmp_k1 = []
for i in range(len(k1)):
    if i == len(k1)-1:
        break
    tmp1 = k1[i]
    tmp2 = k1[i+1]
    try:
        d = (tmp2 - tmp1) / tmp1
    except:
        d = 0
    tmp_k1.append(d)

tmp_k2 = []
for i in range(len(k2)):
    if i == len(k2)-1:
        break
    tmp1 = k2[i]
    tmp2 = k2[i+1]
    try:
        d = (tmp2 - tmp1) / tmp1
    except:
        d = 0
    tmp_k2.append(d)
print(len(tmp_k1))
print(len(tmp_k2))

plt.plot(x,tmp_k1,'s-',color = 'r',label="Pyhop")
plt.plot(x,tmp_k2,'o-',color = 'g',label="Metric-FF")
plt.xlabel("Number of Target")
plt.ylabel("Average Number of Plan Length")
plt.legend(loc = "best")
plt.show()
