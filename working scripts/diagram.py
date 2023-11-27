import os
import exifread
import shutil
import hashlib
from datetime import datetime

local_folder = r"D:\ALL RAW PHOTOS\test"
camera_folder = r"E:\\"


def get_exif_date(file_path):
    with open(file_path, "rb") as file:
        tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
        date_taken = tags.get("EXIF DateTimeOriginal")
        if date_taken:
            return datetime.strptime(str(date_taken), "%Y:%m:%d %H:%M:%S")
        else:
            return None


def organize_files(local_folder):
    for filename in os.listdir(local_folder):
        if filename.lower().endswith("arw"):  # Adjust the file extensions as needed
            file_path = os.path.join(local_folder, filename)
            exif_date = get_exif_date(file_path)

            if exif_date:
                folder_name = exif_date.strftime("%Y-%b-%d")
                folder_path = os.path.join(local_folder, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder_name}")


# Function to find all camera raw paths in a folder and save them to a set.
for path, directories, files in os.walk(camera_folder):
    for file in files:
        if file.lower().endswith("arw"):
            file_path = os.path.join(path, file)
            shutil.copy2(file_path, local_folder)
            print(f"Copied: {file_path} to {local_folder}")
            # exif_date = get_exif_date(file_path)
            # print(exif_date)
            organize_files(local_folder)
