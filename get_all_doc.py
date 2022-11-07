import exifread
import os
import time
import shutil

this_path = os.path.abspath('.')

for root, dirs, files in os.walk(this_path):

    file_list = []
    folder_list = []

    print([root, dirs, files])

    if len(files) > 0:
        print(files)
        for file in files:
            # file_list.append(file)
            if os.path.splitext(file)[-1].upper() == '.JPG':
                file_list.append(file)

    if len(file_list) > 0:

        file_list.sort()

        print(file_list)

        for file in file_list:

            image_datetime = ''

            with open(root + '/' + file, 'rb') as f:
                tags = exifread.process_file(f, stop_tag='UNDEF', details=True, strict=False, debug=False)

                if "EXIF DateTimeOriginal" in tags:
                    timeArray = time.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
                    image_datetime = time.strftime("%Y-%m-%d", timeArray)

                else:
                    image_datetime = time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
                    # print(timeArray)

                if image_datetime not in folder_list:
                    folder_list.append(image_datetime)
                    os.makedirs(root + '\\' + image_datetime)

            f.close()

            shutil.move(root + '\\' + file, root + '\\' + image_datetime + '\\' + file)
