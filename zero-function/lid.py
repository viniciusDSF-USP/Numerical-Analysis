D = abs(int(input("Decimal places of precision: ")))

def trunc(a):
    F = 10**D
    b = abs(a)*F
    return (-1 if a<0 else 1) * (int(b) + (b-int(b)+1/F >= 0.5))/F

a = trunc(float(input("a: ")))
b = trunc(float(input("b: ")))
x0 = a

def f(x):
    return trunc(x**3 - 6*x**2 + 2)

def g(x):
    return trunc(((x**3+2)/6)**0.5)

print(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}} {'g(x_k)':^{D+4}}')
print('-'*len(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}} {'g(x_k)':^{D+4}}'))
print(f'{0:<3} {x0:>{D+4}.{D}f} {f(x0):>{D+4}.{D}f} {g(x0):>{D+4}.{D}f}')

if (abs(g(x0)-x0) < 10**(-D)):
    print(f'Finded root at {x0:.{D}f} in 0 iterations')
else:
    k = 1
    kmax = int(1e6)
    xk = g(x0)

    while (k < kmax):
        print(f'{k:<3} {xk:>{D+4}.{D}f} {f(xk):>{D+4}.{D}f} {g(xk):>{D+4}.{D}f}')

        if (abs(g(xk)-xk) < 10**(-D)): # Found 0 with D decimal places of precision
            print('Converged: error below tolerance!')
            break
        
        elif (xk == x0): # Avoids loop due to truncation error accumulation
            print('Converged: due to repeated xk!')
            break

        elif (not (a <= xk <= b)):
            print("Didn't converged: xk is out of range!")
            break
        
        k += 1
        x0 = xk
        xk = g(xk)
    
    if (k == kmax):
        print('Root took too long to converge!')
    elif (a <= xk <= b):
        print(f'Finded root at {xk:.{D}f} in {k} iterations')