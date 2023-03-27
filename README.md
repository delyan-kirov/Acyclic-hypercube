# Acyclic-hypercube
A repository for the boolean lattice project.

The bash script make.sh takes input n the size of the hypercube Q(n) with 2**n vertices. It then creates a conjure model which is solved in minion. The results are fed to GAP, which removes isomorphic classes and cyclic digraphs. The program will tell you how many DAGs (Directed Acyclic Graphs) there are which base graph Q(n) and create a GAP workspace.

# How to use
You can open the workspace by typing:
gap -L workspace.g
Inside the terminal, assuming there is a path to GAP. 

The graphs are contained inside a list called DAGs. Visualisation tools are available. In terminal type:
Splash(DotDigraph(DAGs[i]));
Where i is from 1 to length(DAGs). This will open a pdf file with the picture of the DAG. You can also:
Print(DotDigraph(DAGs[i]));
PrintTo("DAG1.txt", DotDigraph(DAGs[i]));
To print in text form and save as text file. 

# Required packages
The following are necessary (but potentially not sufficient):
1. Python3 and a package manager like pip.
2. Conjure, Savilerow, minion (potentially other solvers)?
3. GAP (The package "digraphs" and its dependencies). 
4. Paths to conjure, minion, savilerow, gap, bash

# ToDo:
1. Improve the SAT model. Currently, the SAT model creates many isomorphic images, this could potentially be reduced. Perhaps there is also a better way to remove cycles as well. 
2. Calculate in GAP (or python) the number of RSE faces and sinks. 
3. Reduce unneeded python dependencies. 
