from pulp import *


x = LpVariable("x", 0, 3)
y = LpVariable("y", 0, 1)

prob = LpProblem("myProblem", LpMinimize)
prob += x + y <= 2

prob += -4*x + y

status = prob.solve()

value(x), value(y)

value(prob.objective)

print(value(x),value(y))
