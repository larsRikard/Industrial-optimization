from gekko import GEKKO
#https://stackoverflow.com/questions/39236863/restrict-scipy-optimize-minimize-to-integer-values
m = GEKKO(remote=False)
x = m.Array(m.Var,9,lb=0,ub=7,integer=True)

def f(x):
    return (481.79/(5+x[0]))+(412.04/(4+x[1]))\
           +(365.54/(3+x[2]))+(375.88/(3+x[3]))\
           +(379.75/(3+x[4]))+(632.92/(5+x[5]))\
           +(127.89/(1+x[6]))+(835.71/(6+x[7]))\
           +(200.21/(1+x[8]))

m.Minimize(f(x))
m.Equation(sum(x)==7)
m.options.SOLVER=1
m.solve()
print(x)