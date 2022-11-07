import exifread
import os
import time

file_list = []
folder_list = []

this_path = os.path.abspath('.')

for root, dirs, files in os.walk(this_path):
    for file in files:
        # file_list.append(file)
        if os.path.splitext(file)[-1] == '.jpg':
            file_list.append(file)

file_list.sort()

# print(file_list)

for file in file_list:

    image_datetime = ''

    with open(file, 'rb') as f:
        tags = exifread.process_file(f, stop_tag='UNDEF', details=True, strict=False, debug=False)

        # if "Image DateTime" in tags:
        #     timeArray = time.strptime(str(tags['Image DateTime']), "%Y:%m:%d %H:%M:%S")
        #     image_datetime = time.strftime("%Y-%m-%d", timeArray)

        print(tags['EXIF DateTimeOriginal'])
        # print(tags)
