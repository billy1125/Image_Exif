import exifread
import os
import time
import shutil

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

        if "Image DateTime" in tags:
            timeArray = time.strptime(str(tags['Image DateTime']), "%Y:%m:%d %H:%M:%S")
            image_datetime = time.strftime("%Y-%m-%d", timeArray)

        else:
            image_datetime = time.strftime("%Y-%m-%d", time.localtime(os.stat(file).st_mtime))
            # print(timeArray)

        if image_datetime not in folder_list:
            folder_list.append(image_datetime)
            os.makedirs(this_path + '/' + image_datetime)

    f.close()

    shutil.move(this_path + '/' + file, this_path + '/' + image_datetime + '/' + file)

# print(folder_list)

# for folder_name in folder_list:
#     os.makedirs(this_path + '/' + folder_name)
