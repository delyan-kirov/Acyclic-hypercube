# %%
import functools

#%%
def equalities (variables) -> str:
    pairs = []
    constraints = []
    for i in range (len(variables)-1): pairs.append((variables[i], variables[i+1]))
    for i, j in pairs: 
        if(j != ("a" + str(len(variables) - 1))):
            constraints.append("!(" + i + " = " + j + ")" + " /\\ " )
        else: constraints.append("!(" + i + " = " + j + ")")

    constraints = functools.reduce(lambda i, j : i + j, constraints, "")
    constraints = "(" + constraints + ")"
    
    return constraints
#%%
def conjuncts (variables) -> str:
    forAllai = []
    n = len(variables)
    constraints = []
    # forAllai = variables.copy()
    # "exists i:N. forAll k:N. (C((k,i)) = 0)"
    forAllai = list(map(lambda i: "(C((k," + i + ")) = 0)", variables))

    for element in forAllai[:-1]:
        constraints.append(element + " /\\ ")
    
    constraints.append(forAllai[-1])
    constraints = functools.reduce(lambda i, j : i + j, constraints, "")
    constraints = "(forAll k:N. (" + constraints + "))"
    
    return constraints
# %%
#Do something in this block. 
def parse (PeakNumber : int) -> str:
    # "exists i:N. forAll k:N. (C((k,i)) = 0)"
    variables = list (map(lambda i: "a" + i, list (map (str, range(PeakNumber + 1))))) # a1 a2 a3 ...
    variablesCopy = variables.copy()
  
    variables = list(map(lambda i: i + ", ", variables)) #a1, a2, ...
    variables = (functools.reduce(lambda i, j : i + j, variables, "")) #reduce list to string
    variables = variables[:-2] #remove final ,

    data:str = "exists " + functools.reduce(lambda i, j : i + j, variables, "") + ":N. "
    equalities_ai = equalities(variablesCopy)
    conjuncts_ai = conjuncts(variablesCopy)

    data = data + equalities_ai + " /\\ " + conjuncts_ai

    return data
# %%
# main
PeakNumber = int (input("How many peeks are you interested in? \n"))

peaksConstr = parse(PeakNumber)
data:str = ""
with open("boolean.essence", 'r') as file:
      data += file.read()
      file.close()
data = data + "\n" + peaksConstr

with open("booleanPeaks.essence", 'w') as file:
      file.write(data)
      file.close()