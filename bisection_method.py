import tabulate
Data=[]
data=[]
def bisection(func,a,b,error_accept):
    def f(x):
        f = eval(func)
        return f
    error=b-a
    if(f(a)*f(b)>=0 and a>=b):
        print("wrong a,b")
        return;
    x=a
    n = 0
    while error>=error_accept:
        data.append(n)
        n=n+1
        data.append(str(a))
        data.append(str(b))
        x = (a + b) / 2
        data.append(str(x))
        data.append(str(f(x)))
        if f(x) == 0:
            break
        elif f(x) * f(b) < 0:
            a = x
        elif f(a) * f(x) < 0:
            b = x
        c=data.copy()
        Data.append(c)
        error=b-a
        data.clear()
    print("The root is %0.4f"%x)


bisection('2.71828**x-3*x',1.5,1.6,0.001)
print(tabulate.tabulate(Data,headers=['n','a','b','x','f(x)'],tablefmt='fancy_grid'))




