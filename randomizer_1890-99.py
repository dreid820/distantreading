import os, random
import shutil

#Set source directory and output directory
src_dir = 'E:/1890_1899'
out_dir = 'E:/randomized_files_1890-99/'

#Randomly choose a subdirectory from the source directory. Move that random
#subdirectory to the output directory, but not if it has already been chosen.
for num in range(1000):
    ran_fol = random.choice(os.listdir(src_dir))
    if ran_fol not in out_dir:
        shutil.move('E:/1890_1899/'+ran_fol, out_dir)