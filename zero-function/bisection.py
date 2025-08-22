D = abs(int(input("Decimal places of precision: ")))

a = int(input("a: "))
b = int(input("b: "))

def trunc(a):
    F = 10**D
    b = abs(a)*F
    return (-1 if a<0 else 1) * (int(b) + (b-int(b)+1/F >= 0.5))/F

def f(x):
    return trunc(x**3 - 6*x**2 + 2)

print(f'{'k':<3} {'x_k':>7} {'f_k':>7} {'I':^7}')
print('-'*30)
print(f'{0:<3} {a:>{D+4}.{D}f} {f(a):>{D+4}.{D}f} {'-;-':>7}')
print(f'{1:<3} {b:>{D+4}.{D}f} {f(b):>{D+4}.{D}f} {'-;-':>7}')

if (f(a) == 0):
    print(f'Finded root at {a:.{D}f} in 0 iterations')
elif (f(b) == 0):
    print(f'Finded root at {b:.{D}f} in 1 iteration')
elif (f(a)*f(b) > 0):
    print(f"There's no root between {a} and {b}")
else:
    k = 2
    kmax = int(1e6)
    x0 = trunc((a+b)/2)
    xk = x0
    i = 0
    j = 1

    while (k < kmax):
        print(f'{k:<3} {xk:>{D+4}.{D}f} {f(xk):>{D+4}.{D}f} {f'{i}:{j}':>7}')

        if (abs(f(xk)) < 10**(-D)): # Find 0 with D decimal places of precision
            print('Converged: error below tolerance!')
            break
        
        if (xk == a or xk == b): # Avoids loop due to truncation error accumulation
            xk = x0
            print('Converged: due to repeated xk!')
            break

        if (f(a)*f(xk) < 0):
            b = xk
            j = k
        elif (f(xk)*f(b) < 0):
            a = xk
            i = k
        
        k += 1
        x0 = xk
        xk = trunc((a+b)/2)
    
    if (k == kmax):
        print('Root took too long to converge!')
    else:
        print(f'Finded root at {xk:.{D}f} in {k} iterations')