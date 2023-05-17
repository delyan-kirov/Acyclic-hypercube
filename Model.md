# Hypercube, Peak and RSE face model



## RSE faces

    There exists points (a1, a2, a3, a4), (b1, b2, b3, b4).., (c1, c2, c3, c4) in domain N.
    
Four points per face. Such that:


### Non degenerate:

    (a1 != a4) and (a2 != a3) and 
    
    (b1 != b4) and (b2 != b3) and
    
    ... and
    
    (c1 != c4) and (c2 != c3)


### RSE constraint

    Direction(a1, a2) = 1 and
    
    Direction(a1, a3) = 1 and
    
    Direction(a4, a2) = 1 and
    
    Direction(a4, a3) = 1 and

This makes sure that all points are unique as well.


### Uniqueness

    Does not exist points x1, x2, x3, x4 in domain N st:
    
The points form an RSE face:

    Direction(x1, x2) = 1 and
    
    Direction(x1, x3) = 1 and
    
    Direction(x4, x2) = 1 and
    
    Direction(x4, x3) = 1 and
    
Are not degenerate:

    (x1 != x4) and (x2 != x3)

And do not everlap other found points:

    (x1 != a1) and (x2 != a2) and (x3 != a3) and (x4 != a4) and
    
    (x1 != b1) and (x2 != b2) and (x3 != b3) and (x4 != b4) and
    
    ...
    
    (x1 != c1) and (x2 != c2) and (x3 != c3) and (x4 != c4)



## Peaks

    There exists points a1, a2.., an in domain N st:

The points are unique:

    (a1 != a2) and (a1 != a3) and ... and (a1 != an) and
    
    (a2 != a3) and (a2 != a4) and ... and (a2 != an) and
    
    ... and
    
    (a{n-1} != an)
    
The points are Peaks

    for all points i in domain N: direction(a1, i) = 0 and
    
    for all points i in domain N: direction(a2, i) = 0 and
    
    ... and
    
    for all points i in domain N: direction(an, i) = 0 and



## Acyclic

For Q(n) the hypercube of with 2^n vertices, the graph contains 4, 6, 8,.., 2^n cycles for n>1. [https://en.wikipedia.org/wiki/Hypercube_graph]. 

The following must be false

### Cycles

    exists four points a1, a2, a3, a4 in domain N :
        Direction(a1, a2) = 1 and Direction(a2, a3) = 1 and Direction(a3, a4) = 1 and
        Direction(a4, a1) = 1
        
    and
        
    exists six points b1 to b8 in domain N :
        Direction(b1, b2) = 1 and Direction(b2, b3) = 1 and ... and Direction(b8, a1) = 1
        
    and
    
    exists 2^n points c1 to c{2^n} in domain N :
        Direction(c1, c2) = 1 and Direction(c2, c3) = 1 and ... and
        Direction(c{2^n}, a1) = 1
        
### Uniqueness
    
I think this might be enough because Direction(a1, a1) = 0 already. So (a1 != a2) and (a2 != a3) and if
Direction (a1, a2) = 1 then Direction (a2, a1) = 0 so (a1 != a3)?
