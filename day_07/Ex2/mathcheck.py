import numpy as np
S = np.array([[-1,0,0],[1,-1,1],[0,2,-2]])
k = np.array([100, 0.25, 1])
c_0 = np.array([1,0,0])
print(k*c_0)
print([k[i]*c_0[i] for i in range(len(k))])
reac = k*c_0
RHS = S*reac
print("mult with * \n",RHS)
print("mult with matmul \n",np.matmul(S,reac))