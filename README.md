# JANIS-2-MCNP
Convert JANIS cross section csv files to MCNP formated tally multipliers for F4 or FMESH4 tallies.

## Usage
./janis2fmesh.py [input csv] [fmesh number] [rowsize] [min energy] [max energy]

default: ./janis2fmesh.py table.csv 4 128 0 100

## How to obtain the data
On the http://www.oecd-nea.org/janisweb website, export the cross-sections of interest in CSV format.
Use this converter to generate an MCNP formated tally multiplier for a F4 or FMESH4 tally.
Use the FACTOR=... on the FMESH to multiply by the atom density
