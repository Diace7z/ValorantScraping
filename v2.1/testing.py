import random
r = 0.1
step = int(1/r)
init = random.sample(range(0,step),k=1)[0]

a = [1*x for x in range(1,100)]
print(a[0:-1:2])



