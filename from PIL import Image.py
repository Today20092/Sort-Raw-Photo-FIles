from PIL import Image
from PIL.ExifTags import TAGS


def get_date_taken(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        return value
    except Exception as e:
        print(f"Error: {e}")
    return None


# Example usage
file_path = "D:\ALL RAW PHOTOS\01-31-2023\SON06863.ARW"
date_taken = get_date_taken(file_path)

if date_taken:
    print(f"Date Taken: {date_taken}")
else:
    print("Unable to retrieve date taken.")
