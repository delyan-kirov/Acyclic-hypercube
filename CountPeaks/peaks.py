# %%
import functools

#%%
def addConjunction (list):
    result = ""
    for item in list:
        result += (item + " /\ ")
    result = result[:-3]
    return result
        

#%%
def productPairs (vecR, vecL):
     return [(left,right) for i, right in
            enumerate(vecR) for j, left in
            enumerate(vecL) if (i != j)]

#%%
def equalities (variables) -> str:
    pairs = []
    constraints = []
    pairs = productPairs(variables, variables)

    for i, j in pairs: 
        if(pairs[-1] != (i,j)):
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
    # "exists i:N. forAll k:N. (C((i,k)) = 0)"
    forAllai = list(map(lambda i: "(C((" + i + ",k)) = 0)", variables))

    for element in forAllai[:-1]:
        constraints.append(element + " /\\ ")
    
    constraints.append(forAllai[-1])
    constraints = functools.reduce(lambda i, j : i + j, constraints, "")
    constraints = "(forAll k:N. (" + constraints + "))"
    
    return constraints

def uniqueness(points):
    
    """
    given a1, a2, a3... being peaks
    if b is a peak then b is equal to a1 or
    b is equal to a2 or ...
    """
    comparisons = []
    
    for p in points:
        comparisons.append("!(" + p + " = b)")
    
    comparisons = addConjunction(comparisons)
    constraint = "!(exists b : N. (forAll k:N. (C((b,k)) = 0)) /\ " + comparisons + ")"
    return constraint
# %%
#Do something in this block. 
def parse (PeakNumber : int) -> str:
    # "exists i:N. forAll k:N. (C((k,i)) = 0)"
    variables = list (map(lambda i: "a" + i, list (map (str, range(PeakNumber + 1))))) # a1 a2 a3 ...
    variablesCopy = variables.copy()
    
    """
    given a1, a2, a3... being peaks
    if b is a peak then b is equal to a1 or
    b is equal to a2 or ...
    """
  
    variables = list(map(lambda i: i + ", ", variables)) #a1, a2, ...
    variables = (functools.reduce(lambda i, j : i + j, variables, "")) #reduce list to string
    variables = variables[:-2] #remove final ,

    data:str = "exists " + functools.reduce(lambda i, j : i + j, variables, "") + ":N. "
    equalities_ai = equalities(variablesCopy)
    conjuncts_ai = conjuncts(variablesCopy)
    uniqueConst = uniqueness(variablesCopy)

    data = data + equalities_ai + " /\\ " + conjuncts_ai + " /\ \n" + uniqueConst + ","
    if (PeakNumber == 0):
        data = "exists a0:N. (forAll k:N. ((C((a0,k)) = 0)))" + " /\ \n" + uniqueConst + ","
    return data
# %%
# main
PeakNumber = int (input("How many peeks are you interested in? \n")) - 1

uniqueness(["a1", "a2", "a3", "a4"])

peaksConstr = parse(PeakNumber)
    
data:str = ""
with open("boolean.essence", 'r') as file:
      data += file.read()
      file.close()
data = data + "\n" + peaksConstr

with open("booleanPeaks.essence", 'w') as file:
      file.write(data)
      file.close()

#The script does not guarantee exactly n peaks, only at least n peaks. 