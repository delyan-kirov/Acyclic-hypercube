# %%
from functools import reduce

# %%
"""One RSE face. Exists a1, a2, a3, a4 : N. a1 -> a2, a1 -> a3, a4 -> a3, a4 -> a2
Two RSE faces. Exists a1, a2, a3, a4, a5, a6, a7, a8 : N. (a1 -> a2), (a1 -> a3), (a4 -> a2), (a4 -> a3) ; 
                                                          (a5 -> a6), (a5 -> a7), (a8 -> a6), (a8 -> a7) ;
should be C((a,b)) not (a -> b)
"""

#%%
def clearFlatten (string):
    result = [x.strip() for x in string.split(',')]
    return result

#%%
def addConjunction (list):
    result = ""
    for item in list:
        result += (item + " /\ ")
    result = result[:-3]
    return result
        
#%%
# Generates a pair of vectors, one containing points, the other containing constraints
def genPairs (offset):
    basePairs = map(lambda x : x + 4 * offset, [1,2,3,4])
    basePairs = map(lambda x : "a" + str(x), basePairs)

    edges = map(lambda x : x + 4 * offset, [1,2,1,3,4,2,4,3])
    edges = list(map(lambda x : "a" + str(x), edges))
    edges = [(edges[i], edges[i+1]) for i in range (0, len(edges), 2)]
    
    constraints = []
    for i in range (0, len(edges)):
        constraints.append("(C((" + str(edges[i][0]) + ", " + str(edges[i][1]) + ")) = 1) /\ ")
        
    constraints = reduce(lambda x, y: x + y, constraints)
    points = ""
    basePairs = list(basePairs)
    
    for i in range (0, len(basePairs)):
        if (i == len(basePairs) - 1):
            points += str(basePairs[i])
            break
        points += str(basePairs[i]) + ", "

    return (points, constraints)

#%%
def comparisons(points):
    if len(points) <= 4:
        return (["!(a1 = a2)"])
    else:
        compList = []
        for i in range(0, len(points)-4, 4):
            compList.append((points[i], points[i+4]))
            
    constraints = []
    for pair in compList:
        constraint = "!(" + str(pair[0]) + " = " + str(pair[1]) + ")"
        constraints.append(constraint)
    return constraints
#%%
def uniqueness(points):
    """
    Given a1, a2, a3, a4...
    the following is false {
        exist b1, b2, b3, b4 st
            (b1 -> b2), (b1 -> b3), (b4 -> b2), (b4 -> b3)
            (b1 != a1) and (b1 != a2)...
    """
    B = "b1, b2, b3, b4"
    BRSEFaces = "( (C((b1,b2)) = 1) /\ (C((b1,b3)) = 1) /\ (C((b4,b2)) = 1) /\ (C((b4,b3)) = 1) )"
    comparisons = []
    
    for p in points:
        comparisons.append("!(" + p + " = b1)")
    
    comparisons = addConjunction(comparisons)
    constraint = "exists " + B + " : N. " + BRSEFaces + " /\ (" + comparisons + ")"
    constraint = "!(" + constraint + ")"
    return constraint

#%%
# Generate constraints that ensure that each 4-tuples of points are unique in an RSE face
def genUniqueFaces (points):
    pairs = []
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            constraint = "!(" + str(points[i]) + " = " + str(points[j]) + ")"
            pairs.append(constraint)
    return addConjunction(pairs)

#%%
def build(n):
    points = ""
    constraints = ""
    
    for i in range(0,n):
        if (i == 0):
            points += (genPairs(i))[0]
            constraints += (genPairs(i))[1]
            continue
        points += ", " + (genPairs(i))[0]
        constraints += (genPairs(i))[1]
    
    constraints = constraints[:-3]
    equalities = addConjunction(comparisons(clearFlatten(points)))
    
    uniqueRSEfaces = []
    for i in range (0,len(points)):
         uniqueRSEfaces.append(genUniqueFaces(clearFlatten(points)[i:i+4]))
    uniqueRSEfaces = [i for i in uniqueRSEfaces if i != ""]
    uniqueRSEfaces = addConjunction(uniqueRSEfaces)
    
    # likely a problem here, make sure /\ is placed everywhere
    
    result = "exists " + points + " : N. " + "(" + equalities + ")" \
        + " /\ \n " + "(" + uniqueRSEfaces + ")" \
        + " /\ \n " + "(" + constraints + ")"
    uniqueConst = uniqueness(clearFlatten(points))
    result += " /\ \n " + uniqueConst
    
    return result
    
# %%
# main
rseFaceNumber = int (input("How many RSE faces are you interested in? \n"))
rseFaces = build(rseFaceNumber)

# with open("boolean.essence", 'r') as file:
#       data = file.read()
#       file.close()
# data = data + "\n" + rseFaces

with open("booleanPeaks.essence", 'a') as file:
      file.write("\n" + "\n$RSE faces \n" + rseFaces)
      file.close()

#%%
# notes
"""
The script as it is only creates constraints for at least n number of RSE faces,
not exactly n number of faces. More constraints need to be given on top of these.
There does not exist a face which is different from the one listed. 
"""
"""
When comparing points from different faces, only one comparison is needed not all
points need to be different, currently too many comparisons are being made (done)
"""
"""
The code could be a little better and it's probably worth cleaning eventually. 
"""