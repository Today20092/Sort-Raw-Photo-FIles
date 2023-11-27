import os
import hashlib

camera_folder = r"D:\ALL RAW PHOTOS\test"
# local_folder =

# camera_raw_files = dict()
# local_raw_files = dict()
unique_files_on_camera = dict()


# this section go into each file in the os.walk folder and determines its path, its hash and adds it to the dictionary which assocaites the hash -> file path

# this section also checks if the file path has already been added to dictionary and it tells you if the file is a duplicate

for path, directories, files in os.walk(camera_folder):
    for file in files:
        # if file.lower().endswith("arw"):
        file_path = os.path.join(path, file)
        print(f"The file path is: {file_path}")

        # Converting all the content of our file into md5 hash. rb means read binary, meaning it will read its content and it is not affeced by the title.
        Hash_file = hashlib.md5(open(file_path, "rb").read()).hexdigest()
        print(f"The hash is: {Hash_file}")

        # this section adds each file path & its has to the dictionary and if it finds the same hash_file [hexidecmial] in the dictionary it then says it is a duplicate
        if Hash_file not in unique_files_on_camera:
            unique_files_on_camera[
                Hash_file
            ] = file_path  # the has file is the hexidecmial key, and it is now assoicated with the file path. basically a dictionary.
        else:
            print(f"{file_path} is a DUPLICATE!!!!")
