import time

def loop4(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count+=1
    return count

i = 100
while (i <= 819200):
    t1 = time.time()
    for j in range(40):
        loop4(i)
    t2 = time.time()
    print("i: ", i, "-time:", (t2-t1) * 1000)
    i*=2
    