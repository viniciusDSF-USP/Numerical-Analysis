D = abs(int(input("Decimal places of precision: ")))

def trunc(a):
    F = 10**D
    b = abs(a)*F
    return (-1 if a<0 else 1) * (int(b) + (b-int(b)+1/F >= 0.5))/F

a = trunc(float(input("a: ")))
b = trunc(float(input("b: ")))
quant = int(input("How many roots: "))
x0 = a
x1 = b
zeros = []

def f(x):
    return trunc(x**3 - 5*x)

def h(x):
    den = 1
    for v in zeros: den *= (x-v)
    return trunc(f(x)/den)

def g(x0,x1):
    return trunc((h(x1)*x0 - h(x0)*x1)/(h(x1)-h(x0)))

print(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}}')
print('-'*len(f'{'k':<3} {'x_k':^{D+4}} {'f(x_k)':^{D+4}}'))
print(f'{0:<3} {x0:>{D+4}.{D}f} {f(x0):>{D+4}.{D}f}')
print(f'{1:<3} {x1:>{D+4}.{D}f} {f(x1):>{D+4}.{D}f}')

k = 2
kmax = int(1e6)

for _ in range(quant):
    x0 = a
    x1 = b

    if (abs(f(x0)) < 10**(-D)):
        print(f'Finded root at {x0:.{D}f} in 0 iterations')
    elif (abs(f(x1)) < 10**(-D)):
        print(f'Finded root at {x1:.{D}f} in 1 iterations')
    elif (abs(f(x1)-f(x0)) < 10**(-D)):
        print("Didn't converged: divison by zero!")
    else:
        xk = g(x0,x1)

        while (k < kmax):
            print(f'{k:<3} {xk:>{D+4}.{D}f} {f(xk):>{D+4}.{D}f}')

            if (abs(f(xk)) < 10**(-D) or abs(xk-x1) < (1+abs(x1))*10**(-D)): # Found 0 with D decimal places of precision or Relative error
                print('Converged: error below tolerance!')
                zeros.append(xk)
                break
            
            elif (xk == x1): # Avoids loop due to truncation error accumulation
                print('Converged: due to repeated xk!')
                zeros.append(xk)
                break

            elif (abs(f(x1)-f(x0)) < 10**(-D)):
                print("Didn't converged: divison by zero!")
                break

            #elif (not (a <= xk <= b)):
            #    print("Didn't converged: xk is out of range!")
            #    break
            
            k += 1
            x0, x1 = x1, xk
            xk = g(x0,x1)
        
        if (k == kmax):
            print('Root took too long to converge!')
        elif (a <= xk <= b):
            print(f'Finded root at {xk:.{D}f} in {k} iterations')
            k += 1

print(f'Roots found: [{', '.join( [f'{v:.{D}f}' for v in zeros] )}]')