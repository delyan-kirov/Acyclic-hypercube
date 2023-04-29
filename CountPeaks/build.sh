#!/usr/bin/env bash
python3 lattice.py
#python3 peaks.py
python3 RSE.py

conjure solve booleanPeaks.essence n.param

rm n.param
#rm booleanPeaks.essence

# conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all boolean1.essence n.param 
