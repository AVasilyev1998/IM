#!/bin/bash
. venv/bin/activate
# normal params 7 5 0.5 3500 3 2
python simulation.py $1 $2 $3 $4 $5 $6
python view_statistics.py
