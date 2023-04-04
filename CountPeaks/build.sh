#!/usr/bin/env bash
python3 lattice.py
python3 peaks.py

conjure solve booleanPeaks.essence n.param

rm n.param
