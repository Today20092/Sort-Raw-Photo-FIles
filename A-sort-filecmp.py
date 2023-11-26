import filecmp
import os
import shutil
import exifread

local_folder = r"D:\ALL RAW PHOTOS\test"
camera_folder = r"E:\\"


for path, directories, files in os.walk(local_folder):
    for raw_file in files:
        if raw_file.lower().endswith("arw"):
            local_raw_file = os.path.join(path, raw_file)
            camera_raw_file = os.path.join(camera_folder, raw_file)

            if os.path.exists(camera_raw_file):
                file_are_equal = filecmp.cmp(local_raw_file, camera_raw_file)

                if files_are_equal:
                    print(
                        f"The files {local_raw_file} and {camera_raw_file} are identical."
                    )
                else:
                    print(
                        f"The files {local_raw_file} and {camera_raw_file} are different."
                    )
