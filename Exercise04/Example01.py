import control as cnt
from numpy import reshape
A = 3
B = 1
R = 1
Q = 2
print("controller found: ", cnt.lqr(A, B, Q, R))