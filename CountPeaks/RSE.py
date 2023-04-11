# %%
import math

# %%
#Do something in this block. 
#One RSE face. Exists a1, a2, a3, a4 : N. a1 -> a2, a1 -> a3, a4 -> a3, a4 -> a2
#Two RSE faces. Exists a1, a2, a3, a4, a5, a6, a7, a8 : N. (a1 -> a2), (a1 -> a3), (a4 -> a2), (a4 -> a3) ; 
#                                                          (a5 -> a6), (a5 -> a7), (a8 -> a6), (a8 -> a7) ;

#%%
def genPairs (offset):
    basePairs = map(lambda x : x + 4 * offset, [1,2,3,4])
    basePairs = map(lambda x : "a" + str(x), basePairs)

    edges = map(lambda x : x + 4 * offset, [1,2,1,3,4,2,4,3])
    edges = list(map(lambda x : "a" + str(x), edges))
    edges = [(edges[i], edges[i+1]) for i in range (0, len(edges), 2)]

    return (list(basePairs), list(edges))

# %%
# main
offset = 1
result = genPairs(offset)
print (result)
