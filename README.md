# Acyclic-hypercube

A repository for the boolean lattice project.

The bash script make.sh takes input n the size of the hypercube Q(n) with 2**n vertices. It then takes as input the number of desired peeks and RSE faces. 

# How to use
Run the bash script:

    build.sh
    
This will automatically activate the local python environment hypercube. You can also connect to the env with:

    source ./hypercube/bin/activate

# Required packages
1. Minion
2. SavileRow
3. Conjure
4. GAP for visualization?

# ToDo:
1. Test the model for mistakes.
2. Add a break cycles clause. Perhaps implement something better?
