import control as cnt
from numpy import reshape, shape, linalg
i = complex(0, 1)

# defining sytem matrices
A = [[0, 1, 0], [0, 0, 1], [-1, -5, -6]]
B = [[0], [0], [1]]

# check whether the system is controllable
C = cnt.ctrb(A, B)
det = linalg.det(C)
print('system\'s determinant is ', det)
if abs(det) > 1e-5:
    print('system is controllable')
else:
    print('system is not controllable')

# poles where given
p = [-2+4*i, -2-4*i, -10]
K = cnt.place(A, B, p)

# output to check if the poles are correct
print('controller: ', K)
A = [0, 0, 1, 0, 1, -6, 1, -6, 31]
A = reshape(A, (3, 3))
print(shape(A))
print(A)