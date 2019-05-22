#!/usr/bin/env python

#Small automation Python - Search .pdf file or any file on HD, and then auto move file to USB.
#Created by Tommas Huang 
#Created date: 2019-05-22

import os
#Python OS module provides easy functions that allow us to interact 
#and get Operating System related information and even control processes up to a limit.
import shutil
#The shutil module offers a number of high-level operations on files and collections of files.
#In particular, functions are provided which support file copying and removal.


def move_all_ext(extension, source_root, dest_dir):
    # Recursively walk source_root
    for (dirpath, dirnames, filenames) in os.walk(source_root):
        # Loop through the files in current dirpath
        for filename in filenames:
            # Check file extension
            if os.path.splitext(filename)[-1] == extension:
                # Move file
                shutil.move(os.path.join(dirpath, filename), os.path.join(dest_dir, filename))


# Move all pdf or any docx..etc files from A: to USB Drive.
move_all_ext(".pdf", "/Users/tommashuang/Documents/A", "/Volumes/KODAK/B")