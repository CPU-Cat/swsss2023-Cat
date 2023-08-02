from numpy.linalg import norm
import matplotlib.pyplot as plt
import numpy as np
"""
Created on Tue Aug 1 2023

@author: CPU-Cat ckpawu@bu.edu
"""

def explicit_RK_stepper(f,x,t,h,a,b,c):
    """
        Implementation of generic explicit Runge-Kutta update for explicit ODEs
        inputs:
            x - current state 
            t - current time
            f - right-hand-side of the (explicit) ODE to be integrated (signature f(x,t))
            h - step size 
            a - coefficients of Runge-Kutta method (organized as list-of-list (or vector-of-vector))
            b - weights of Runge-Kutta method (list/vector)
            c - nodes of Runge-Kutta method (including 0 as first node) (list/vector)
        outputs: 
            x_runge - estimate of the state at time t+h
    """
    #commented out my attempt to rewrite as class function
    s = len(b)
    k = np.zeros(s)
    for i in range(s): #0,1,2,... s-1
        if i ==0:
            xki = x
            tki = t
        else:
            a_k_vals = []
            for j in range(i):
                a_k_vals.append(a[i-1][j]*k[j]) 
            xki = x +h*np.sum(a_k_vals)
            tki = t+c[i]*h
        k[i] = f(xki, tki)
    onestep = h*np.dot(b,k)
    x_runge = x+onestep

    # k = [f(x,t)]
    # s = len(c)
    # for i in range(s-1):
    #     x_tilde = x+h*np.sum(a[i][j]*k[j] for j in range(len(k)))
    #     k.append(f(x_tilde, t+c[i+1]*h))
    # x_hat = x+h*np.sum(b[i]*k[i] for i in range(len(k)))
    # x_runge = x_hat

    return x_runge # please complete this function 

def integrate(f, x0, tspan, h, step):
    """
        Generic integrator interface

        inputs:
            f     - rhs of ODE to be integrated (signature: dx/dt = f(x,t))
            x0    - initial condition (numpy array)
            tspan - integration horizon (t0, tf) (tuple)
            h     - step size
            step   - integrator with signature: 
                        step(f,x,t,h) returns state at time t+h 
                        - f rhs of ODE to be integrated
                        - x current state
                        - t current time 
                        - h stepsize

        outputs: 
            ts - time points visited during integration (list)
            xs - trajectory of the system (list of numpy arrays)
    """
    t, tf = tspan
    x = x0
    trajectory = [x0]
    ts = [t]
    while t < tf:
        h_eff = min(h, tf-t)
        x = step(f,x,t,h_eff)
        t = min(t+h_eff, tf)
        trajectory.append(x)
        ts.append(t)
    return trajectory, ts

