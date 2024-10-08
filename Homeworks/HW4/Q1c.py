# import libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt



def driver():
    #f = lambda x: (x-2)**3
    #fp = lambda x: 3*(x-2)**2
    #p0 = 1.2
    f = lambda x: sp.special.erf(x / (2 * np.sqrt(0.138e-6 * 5.184e6)))*(35) - 15 
    fp = lambda x: (4375 * np.exp(-(15625 * x**2) / 44712)) / (9 * np.sqrt(138) * np.sqrt(np.pi))

    
    p0 = 0.01
    Nmax = 100
    tol = 1.e-7
    
    print("p0 = 0.01")
    (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)
    
    p0 = 1
    print("p0 = 1")
    (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)


def newton(f,fp,p0,tol,Nmax):
    """
    Newton iteration.
    Inputs:
    f,fp - function and derivative
    p0 - initial guess for root
    tol - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
    Returns:
    p - an array of the iterates
    pstar - the last iterate
    info - success message
    - 0 if we met tol
    - 1 if we hit Nmax iterations (fail)
    """
    p = np.zeros(Nmax+1);
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]
driver()
