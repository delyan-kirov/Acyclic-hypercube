# Report on the state of the boolean lattice problem

Here is a summary of what I've tried for the past while. 



## Generating all possibilities with a SAT solver and pruning symmetric solutions in GAP

The problem here is that even at Q(4) the solutions are just too many, even when we remove 
symmetric solutions from the search. Deleting symmetric solutions seems easy tho.



## Generating the tables from the paper

### Method 1 - Using the boolean lattice

The idea here is to use the boolean lattice model to generate the underlying graph and then
direct the edges. This was done by generating the lattice in python and then directing the 
edges in the SAT solver. The problem here is that prohibiting cycles is difficult this way.

### Method 2 - Generating the DAG without the underlying graph

In this case we are not given the underlying graph, but instead we just ask the solver to 
find a DAG which is also a hypercube. The problem here is generating the hypercube while
also looking for patterns. 

A hypercube Q(n) can be described as a graph which has 2^n vertices, every vertex has degree
n and no cycles of odd length. A directed hypercube should therefore also have an underlying
graph that respects these criteria. Unfortunately, this model blows up. 

### Method 3 - Generating the DAG as a boolean algebra

Here, I use the definition of a boolean algebra to generate the graph and look for the patterns.
Again, The model seems to get too big for the solver to handle. 



## General conclusions

The problem seems difficult to solve using a SAT solving method, because:

1. There are too many solutions and not an efficient way to remove symmetric solutions.
2. Avoiding cycles is difficult to do in a SAT model. 
3. There does not seem to be an easy way to enforce a topological coloring. 

Out of all approaches Method 3 was surprisingly the best. While it still coudn't generate 
anything, the number of constraints could be written succinctly. 

Mothods 2 and 3 were not not able to produce a single solution. 

Method 1 was able to generate all solutions for Q(2) and Q(3). It's quite likely that it 
would be able to produce all solutions for Q(4) within a few months. 

Overall, while looking for the patterns is easy using a SAT approach, the cycles are better 
handled using a more traditional algorithmic approach. 
