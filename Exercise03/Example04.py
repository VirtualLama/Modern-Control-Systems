# observer design through pole placement
import control as cnt
from numpy import reshape, transpose
from numpy.linalg import det
import scipy.signal as sp
A = [0, 1, -2, 3]
A = reshape(A, (2,2))
B = [0, 1]
B = reshape(B, (2, 1))
p = [-3, -4]
Mc = cnt.ctrb(A, B)
Mcdet = det(Mc)
print(Mcdet)
if abs(Mcdet) > 1e-5:
    print('system is controllable')
    K = cnt.place(A, B, p)
    print("K = ", K)
else:
    print("System is not controllable")

# new A for the pole placement
C = [1, 0]
# check observability
Mc = cnt.obsv(A, C)
p2 = [-13, -13]
if abs(det(Mc)) > 1e-5:
    print('system is observable')
    K2 = cnt.place(transpose(A), transpose(C), p2)  # does not work yet
    print("K2 = ", K2)
else:
    print('system is not observable')
