# Sort-Raw-Photo-FIles

The goal of this project is to:
1. automatically import all raw files from my Sony camera into a specific folder when the camera is plugged in
2. rename the files into a specific format
3. Sort them into folders based on the date the image was captured.

## my notes

The python script needs to see if the local folder is missing any files from the camera folder. 

If the local folder is missing files from the camera folder then copy those missing files into the local folder

How can we determine if the local folder has the same files as the camera folder? 

We can use python filecmp. 

We only need to run the function for the files on the camera because those are the files that are important to us. 

All we have to do is compare the files on the camera to what we have locally. 

The files then need to be sorted by the exif date Time created into their own folders on the local folder. 

The function should look something like

for each file that ends in arw in camera folder check local folder for matching file. If matching do not copy. Else copy. 

When function finishes then, move file based on exif data to its own folder. 

When checking the local folder for the files it should check recursively. 


At the end of the script all the folders should look the same and all the photos should be organized the same way without any duplicates or extra folders. 
