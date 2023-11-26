import filecmp
import os
import shutil
import exifread
from datetime import datetime


def get_exif_datetime(file_path):
    with open(file_path, "rb") as file:
        tags = exifread.process_file(file, details=False)
        if "EXIF DateTimeOriginal" in tags:
            return tags["EXIF DateTimeOriginal"].printable
    return None


def check_and_copy_and_organize_files(local_folder, camera_folder):
    # Get a list of files in the local folder
    local_files = [
        file.lower()
        for file in os.listdir(local_folder)
        if file.lower().endswith("arw")
    ]

    # Recursive function to iterate through the files in the camera folder
    def check_and_copy_files_in_folder(folder):
        for path, directories, files in os.walk(folder):
            for raw_file in files:
                if raw_file.lower().endswith("arw"):
                    camera_raw_file = os.path.join(path, raw_file)

                    # Check if the file in the local folder is missing in the camera folder using filecmp
                    for local_file in local_files:
                        local_file_path = os.path.join(local_folder, local_file)
                        if filecmp.cmp(local_file_path, camera_raw_file):
                            break
                    else:
                        # Copy the missing file from the camera folder to the local folder
                        shutil.copy2(camera_raw_file, local_folder)
                        print(
                            f"The file {raw_file} is missing in the local folder and has been copied."
                        )

                        # Get the EXIF datetime of the copied file
                        exif_datetime = get_exif_datetime(
                            os.path.join(local_folder, raw_file)
                        )

                        # Organize the file into a folder based on its EXIF datetime
                        if exif_datetime:
                            exif_datetime = datetime.strptime(
                                exif_datetime, "%Y:%m:%d %H:%M:%S"
                            )
                            destination_folder = os.path.join(
                                local_folder, exif_datetime.strftime("%Y-%b-%d")
                            )
                            os.makedirs(destination_folder, exist_ok=True)
                            destination_file = os.path.join(
                                destination_folder, raw_file
                            )
                            shutil.move(
                                os.path.join(local_folder, raw_file), destination_file
                            )
                            print(
                                f"The file {raw_file} has been organized into {destination_folder}."
                            )

            for directory in directories:
                check_and_copy_files_in_folder(os.path.join(path, directory))

    check_and_copy_files_in_folder(camera_folder)


local_folder = r"D:\ALL RAW PHOTOS"
camera_folder = r"E:\\"

check_and_copy_and_organize_files(local_folder, camera_folder)
