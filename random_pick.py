import os
import random
import shutil

src_folder = r'D:\Humans'
dst_folder = r'D:\MCIT\581\extra project\val\ppl'
num_files = 700

# Get a list of all the files in the source folder
files = os.listdir(src_folder)

# Randomly select 'num_files' files from the list
selected_files = random.sample(files, num_files)

# Copy the selected files to the destination folder
for file in selected_files:
    src_path = os.path.join(src_folder, file)
    dst_path = os.path.join(dst_folder, file)
    shutil.copy(src_path, dst_path)