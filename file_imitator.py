import os
import os.path
from os import path
import shutil

#turn this on if you want to only duplicate files with a specific extension
file_ext_lock = True

#extension suffix of dmc5 efx files
file_ext = "efx.1769672"
print("\nfile extension is set to: " + file_ext + "\n")

#strips the input directory string of single and double quotations if the string has them (os doesn't accept quotations)
def stripper(directory):
    if directory.startswith('"') and directory.endswith('"'):
        directory = input_dir.strip('"')
    elif directory.startswith("'") and directory.endswith("'"):
        directory = input_dir.strip("'")
    return directory

#checks for a folder and creates it if it doesn't exist
def folder_check(folder):
    if not path.exists(folder):
        try: 
            os.mkdir(folder) 
        except OSError as error: 
            print(error)  

current_dir = os.getcwd()

input_dir = current_dir + "\\Input_Immitation"

output_dir = current_dir + "\\Output_Immitation"

#checks if input/output folders exists and creates them if not
folder_check(input_dir)
folder_check(output_dir)

base_file = input("Enter the name of a file that you would like to use as a base (must be in the same folder as file_imitator.py): \n")

file_list = []

batch_files = os.listdir(stripper(input_dir))

#files from the set directory are added to a list
if file_ext_lock == True:    
    for f in batch_files:
        endswith = f.endswith(file_ext)
        if endswith == True:
            file_list.append(f)
else:
    for f in batch_files:
        file_list.append(f)

print("\nimmitating files... \n\n")
for n in file_list:
    new_output = (output_dir + "\\" + n)
    shutil.copyfile(base_file, new_output)
    print("immitated " + n)

print("Complete...")

