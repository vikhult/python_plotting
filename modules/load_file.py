"""
Loads txt files into data containers


@cybertomten
"""
import os
from pathlib import Path
import numpy as np

# ---> Create global variables
cwd = Path.cwd()

# ---> Define necessary methods
def parse_force_disp(data_file):
    with open("Data_File_mod.txt", "w+") as ofile:
        with open("Data_File.txt","r") as ifile:
            for line in ifile:
                split_line = line.split()
                if len(split_line) > 3:
                    ofile.write(concat_line(split_line))
                else:
                    ofile.write(line)
                    
""" Assumes there is an even number on entities in split_line 
which are joined with delimiting whitespace, split_line == list<str>"""                    
def concat_line(split_line):
    tmp_split_line = []
    for kk in range(0,len(split_line)-1,2):
        tmp_split_line.append("_".join(split_line[kk:kk+2]))
    tmp_split_line.append("\n")
    line_str=" ".join(tmp_split_line)
    return line_str

"""   Returns data containers which can be plotted """
def read_data(data_file):
    data_list = []
    with open(data_file,'r') as dfile:
        temp_list = [[],[],[],[]]
        for line in dfile:
            # only valid for space delimited .txt
            split_line = line.split()
            # handle first row title 
            if split_line[0] == "***" and len(data_list) == 0:
                temp_list[0].append(split_line[1])
            
            # handle the intermediate Spam row 
            
            elif split_line[0] == "Spam":
                for kk, jj in zip([0,2,4], [1,2,3]):
                    temp_list[jj].append(split_line[kk]+split_line[kk+1])
                    
            else:
                pass
""" Utilises numpys loadtxt() to return data containers """
def load_data(data_file,mode):
    if mode == "allowed load":
        pass
    elif mode == "force vs. displacement":
        pass
    
# Script execution

if __name__ == "__main__":
    file_list = os.listdir()
    for ent in file_list:
        if ent.split(".")[0] == "Data_File":
            path_to_file = cwd.joinpath(ent)
            #data_container = read_data(path_to_file)
            parse_force_disp(path_to_file)

