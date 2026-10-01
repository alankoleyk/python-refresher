test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

COUNTRY_COL=0
EMISSION_COL=29
DATA=test_fires.csv


run test_exit_code_success python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL $DATA
assert_exit_code 0
 
run test_exit_code_missing_args python3 print_fires.py Afghanistan $COUNTRY_COL
assert_exit_code 2
assert_in_stderr "the following arguments are required"
 
run test_exit_code_invalid_operation python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL $DATA --operation bogus
assert_exit_code 2
assert_in_stderr "invalid choice"
 
run test_exit_code_missing_file python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL nonexistent_file.csv
assert_exit_code 1

#test mean

run test_mean_afghanistan_emission python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL $DATA --operation mean
assert_exit_code 0
assert_in_stdout "2349.676731104636"

#test median

run test_median_afghanistan_emission python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL $DATA --operation median
assert_exit_code 0
assert_in_stdout "2356.3042291316488"


#test stdev

run test_std_afghanistan_emission python3 print_fires.py Afghanistan $COUNTRY_COL $EMISSION_COL $DATA --operation std
assert_exit_code 0
assert_in_stdout "107.94215346585887"
