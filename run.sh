#!/bin/bash

# Example 1: Works correctly
# Valid country, valid column indices, valid file name
python print_fires.py "United States of America" 0 4 Agrofood_co2_emission.csv

# Example 2: Error - invalid column index (not an integer)
python print_fires.py "United States of America" zero 4 Agrofood_co2_emission.csv

# Example 3: Error - file does not exist
# file_name points to a file that isn't there, get_column will catch and report it
python print_fires.py "United States of America" 0 4 nonexistent_file.csv