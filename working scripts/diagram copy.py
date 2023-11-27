import os
import shutil
from datetime import datetime

if __name__ == "__main__":
    local_folder = r"D:\ALL RAW PHOTOS\test"
    camera_folder = r"E:\\"

    # Function to find all camera raw paths in a folder and save them to a set.
    for path, directories, files in os.walk(camera_folder):
        for file in files:
            if file.lower().endswith("arw"):
                file_path = os.path.join(path, file)
                shutil.copy2(file_path, local_folder)
                print(f"Copied: {file_path} to {local_folder}")
