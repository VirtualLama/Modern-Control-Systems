import control as cnt
from numpy import reshape
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('tkagg')

# some random values for the components
L = 1e-5
R = 10
C = 1e-5

# state space metrices
# x1 = Uc
# x2 = dUc/dt
A = [0, 1, -1/(L*C), (-1/(R*C))]
A = reshape(A, (2,2))
B = [0, 1/(L*C)]
B = reshape(B, (2,1))
C = [1, 0]  # x1 is the capacitor voltage
D = 0

T = np.arange(0,1,1e-4)      # to increase the resolution of the plot
sys = cnt.StateSpace(A,B,C,D)   # create the state space system

# create a step response with an initial condition for the
# the capacitor voltage (x1)
[yout, xout] = cnt.step_response(sys, T=T, X0=[1,0])

# create an LQR state feedback controller
Q = [[1,0],[0, 1]]
Q = np.diag([5,5])
R = 1
N = np.zeros((2,2)) # no cross weight values for now

f1 = plt.figure('controlled system')
f2 = plt.figure('state responses')
for i in [0.1]:#[0.01, 0.2, 1, 4]:
    K, S, E =cnt.lqr(A, B, np.diag([i, i]), R)
    print('controller: ', K)
    controlled_sys = cnt.StateSpace(A-B*K, B, C, D)
    print(controlled_sys)
    t,yout2, xout = cnt.step_response(controlled_sys, T=T, X0=[0,0], return_x=True)
    # functions to visualize the output
    #plt.plot(T, yout)
    #plt.plot(T, xout)
    plt.figure('controlled system')
    plt.plot(t, yout2, label=['y,Q=', i])
    for x in xout:
        plt.figure('state responses')
        plt.plot(t,x, label=['states Q=',round(i,3)])

#plt.figure(2)
#plt.plot(xout,yout2)
plt.figure('state responses')
plt.grid(which='both')
plt.legend()
plt.figure('controlled system')
plt.grid(which='both')
plt.legend()
plt.show(block='True')

## TODO: only u can be manipulated, so the change of voltage can not be directly influenced?
# so implement a current controller to change the charge and therefore the du/dt of uc -> second input