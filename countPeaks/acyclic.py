# %%
import os
from pathlib import Path
import math

# %%
def get_n():
    path = Path(__file__).with_name("n.param")
    with path.open() as f:
         data = f.read()
         n = data.split("letting n be ",1)[1]
         f.close()
    return int(n)

# %%
def make_variables(n:int):
     variables = []
     cycles = [2*i for i in range(2,2**(n-1)+1)]
     for i in range(0,len(cycles)):
          variables_i = []
          for j in range(0,cycles[i]):
               variables_i.append ("a" + str(i) + str(j))
          variables.append(variables_i)
     return variables

def conj(cycles:list[str], rel:str):
     conj_all = []
     conj_i = []
     n = len(cycles)
     for i in range(0,n):
          #lattice((i,j))
          conj_i = rel + "((" + cycles[i] + "," + cycles[(i+1) % n] + "))"
          conj_all.append(conj_i)
     return(conj_all)

#%%
def make_clause(lattice:list[str], C:list[str], C_rev:list[str], variables:list[str]):
    n = len(lattice)

    clause = "!(exists "
    for variable in variables: clause += variable + ", "
    clause = clause[:-2] + " :N. ("
 
    for i in range(0,n-1):
         clause = clause + "(" + C[i] + " = 1) " + "/" + "\ "
    clause = clause + "(" + C[n-1] + " = 1)) " + "/" + "\ " + "\n !("

    for i in range(0,n-1):
         clause = clause + "(" + C_rev[i] + " = 1) " + "/" + "\ "
    clause = clause + "(" + C_rev[n-1] + " = 1)))"

    return clause

def make(n):
     constraint = ""
     variables = make_variables(n)
     for variable in variables:
          lattice = conj(variable, "lattice")
          C = conj(variable, "C")
          C_rev = conj(list(reversed(variable)), "C")
          constraint += make_clause(lattice,C,C_rev,variable) + ", \n \n"
     print (constraint)
     return constraint
          
# %%
# main
# Adds SAT constraints to remove cycles and generates a new copy of the SAT model in boolean_copy.essence
n = 3
with open ("cycles.txt", 'w') as f:
     f.write(make(n))
     f.close()

with open ("boolean.essence", 'r') as f:
     boolean_essence = f.read()
     f.close()

with open ("booleanC.essence", "w") as f:
     contence = boolean_essence + "\n " + make(n)
     f.write(contence)
     f.close()