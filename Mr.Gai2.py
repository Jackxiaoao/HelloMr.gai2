import random
b = []
for i in range(50):
    a = random.randint(-10,11)
    b.append(a)
print("整数:",b)
c = []
d = []
for i in b:
    if i > 0:
        c.append(i)
    elif i < 0 :
        d.append(i)
print("正数:",c)
print("负数:",d)
