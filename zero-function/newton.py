D = abs(int(input("Decimal places of precision: ")))

def trunc(a):
    F = 10**D
    b = abs(a)*F
    return (-1 if a<0 else 1) * (int(b) + (b-int(b)+1/F >= 0.5))/F

a = trunc(float(input("a: ")))
b = trunc(float(input("b: ")))
quant = int(input("How many roots: "))
x0 = a
zeros = []

def f(x):
    return trunc(x**3 - 6*x**2 + 2)

def df(x):
    return trunc(3*x**2 - 12*x)

def g(x):
    sub = 0
    for v in zeros: sub += 1/(x-v)
    return trunc(x - 1/(df(x)/f(x) - sub))

print(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}} {'df(x_k)':^{D+4}}')
print('-'*len(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}} {'df(x_k)':^{D+4}}'))
print(f'{0:<3} {x0:>{D+4}.{D}f} {f(x0):>{D+4}.{D}f} {df(x0):>{D+4}.{D}f}')

k = 1
kmax = int(1e6)

for _ in range(quant):
    x0 = a

    if (abs(f(x0)) < 10**(-D)):
        print(f'Finded root at {x0:.{D}f} in 0 iterations')
    elif (abs(df(x0)) < 10**(-D)):
        print("Didn't converged: divison by zero!")
    else:
        xk = g(x0)

        while (k < kmax):
            print(f'{k:<3} {xk:>{D+4}.{D}f} {f(xk):>{D+4}.{D}f} {df(xk):>{D+4}.{D}f}')

            if (abs(f(xk)) < 10**(-D) or abs(xk-x0) < (1+abs(xk))*10**(-D)): # Found 0 with D decimal places of precision or Relative error
                print('Converged: error below tolerance!')
                zeros.append(xk)
                break
            
            elif (xk == x0): # Avoids loop due to truncation error accumulation
                print('Converged: due to repeated xk!')
                zeros.append(xk)
                break

            elif (abs(df(x0)) < 10**(-D)):
                print("Didn't converged: divison by zero!")
                break

            elif (not (a <= xk <= b)):
                print("Didn't converged: xk is out of range!")
                break
            
            k += 1
            x0 = xk
            xk = g(x0)
        
        if (k == kmax):
            print('Root took too long to converge!')
        elif (a <= xk <= b):
            print(f'Finded root at {xk:.{D}f} in {k} iterations')
            k += 1

print(f'Roots found: [{', '.join( [f'{v:.{D}f}' for v in zeros] )}]')