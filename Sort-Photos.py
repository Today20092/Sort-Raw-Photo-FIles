import os
import exifread

folder_path = "D:\ALL RAW PHOTOS"

## this will walk through the paths, directories, and files in the variable "folder_path"
for path, directories, files in os.walk(folder_path):
    ## this will repeat if the files in {files} end in "ARW"
    for raw_file in files:
        if raw_file.endswith("ARW"):
            # print(raw_file)
            ## This joins the path and the file name to create the full path to the arw files
            full_path_raw_files = os.path.join(path, raw_file)
            # print(full_path_raw_files)
