# This program takes the csv file generated by the BMS QuikEval GUI and creates
# a new csv file that can be loaded into a pandas dataframe without errors

from settings import Csv

# Choose file to be converted from csv to pandas data_frame
dc_csv = Csv('discharge_2cells.csv')

lines = dc_csv.to_lines() # split csv into list of lines
divided_lines = dc_csv.to_chars(lines) # split lines into lines of chars
fixed_lines = dc_csv.fix_decimals(divided_lines) # change decimals to be '.'

dc_csv.write_to_file(fixed_lines) #create new cleaned file
