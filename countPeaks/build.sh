#!/usr/bin/env bash
source ./hypercube/bin/activate

python3 lattice.py
python3 constraints.py

conjure solve booleanC.essence n.param

rm n.param
# conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all booleanC.essence n.param 
