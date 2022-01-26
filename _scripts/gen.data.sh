#!/bin/bash

echo "Working on daily emissions for 5 years..."
./emissions.py -r daily -y 5 > data/emissions.daily.5yr.csv &
./emissions.py -r daily -y 5 -c > data/emissions.daily.5yr.c.csv &

echo "Working on daily emissions for 25 years..."
./emissions.py -r daily -y 25 > data/emissions.daily.25yr.csv &
./emissions.py -r daily -y 25 -c > data/emissions.daily.25yr.c.csv &

echo "Working on daily emissions for 100 years..."
./emissions.py -r daily -y 100 > data/emissions.daily.100yr.csv &
./emissions.py -r daily -y 100 -c > data/emissions.daily.100yr.c.csv &

# echo "Working on 200 yr daily emissions..."
# ./emissions.py -r daily -y 200 > data/emissions.daily.200yr.csv &
# ./emissions.py -r daily -y 200 -c > data/emissions.daily.200yr.c.csv &

wait

echo "Completed"