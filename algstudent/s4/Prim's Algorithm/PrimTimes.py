import Helper as help
import Prim as prim
import time

i = 4

elapsed = 0

while elapsed < 600000:
    edges = help.triangularMatrixRandomIntegers(i, 1000, 1000)
    t1 = time.time_ns()
    prim.prim(edges)
    t2 = time.time_ns()
    elapsed = (t2 - t1)/1.e6
    print("n = ", i, " --- time: ", elapsed)
    i*=2