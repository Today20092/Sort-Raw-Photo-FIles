import os
import shutil
import exifread

folder_path = "D:\ALL RAW PHOTOS"

exif_command = "C:\ProgramData\chocolatey\bin\exiftool.exe"

## this will walk through the paths, directories, and files in the variable "folder_path"
for path, directories, files in os.walk(folder_path):
    ## this will repeat if the files in {files} end in "ARW"
    for raw_file in files:
        if raw_file.lower().endswith("arw"):
            # print(raw_file)
            ## This joins the path and the file name to create the full path to the arw files
            full_path_raw_files = os.path.join(path, raw_file)
            # print(full_path_raw_files)

            ## Reads the Exif Data to only see the datetimeoriginal
            with open(full_path_raw_files, "rb") as f:
                tags = exifread.process_file(f)
                datetime_original = tags.get("EXIF DateTimeOriginal")
                if datetime_original:
                    print(f"File: {raw_file}, {datetime_original}")
