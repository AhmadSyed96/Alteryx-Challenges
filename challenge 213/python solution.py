import pandas as pd
from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, GLPK


# obj = [-1, -1, -1, -1, -1, -1, -1, -1]
#
# lhs_ineq = [[2.3, 2.25, 2.53, 2.45, 2.17, 2.15, 2.5, 2.1]]
# rhs_ineq = [950]
#
# bnd = [(40, 80), (40, 80), (40, 80), (40, 80), (40, 80), (40, 80), (40, 80), (30, 40)]
#
# opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
#
# print(opt)

model = LpProblem(name="small-problem", sense=LpMaximize)
a = LpVariable(name="red rose", lowBound=40, upBound=80)
b = LpVariable(name="white daisy", lowBound=40, upBound=80)
c = LpVariable(name="white lilly", lowBound=40, upBound=80)
d = LpVariable(name="red daisy", lowBound=40, upBound=80)
e = LpVariable(name="red carnation", lowBound=40, upBound=80)
f = LpVariable(name="white carnation", lowBound=40, upBound=80)
g = LpVariable(name="spider mum", lowBound=40, upBound=80)
h = LpVariable(name="filler green", lowBound=30, upBound=40)
model += (2.3*a + 2.25*b + 2.53*c + 2.45*d + 2.17*e + 2.15*f + 2.5*g + 2.1*h <= 950, "price constraint")
model += lpSum([a, b, c, d, e, f, g, h])
status = model.solve()


table = pd.Series({var.name : var.value() for var in model.variables()}).reset_index()
table.columns = ['Flower', 'Price']
print(table)
# print(f"objective: {model.objective.value()}")
# for var in model.variables():
#     print(f"{var.name}: {var.value()}")
