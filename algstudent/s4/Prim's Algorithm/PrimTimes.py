import Helper as help
import Prim as prim
import time

i = 4

while i < 2049:
    edges = help.triangularMatrixRandomIntegers(i, 1, 10)
    t1 = time.time_ns()
    prim.prim(edges)
    t2 = time.time_ns()
    elapsed = (t2 - t1)/1.e6
    print("n = ", i, " --- time: ", elapsed)
    i*=2