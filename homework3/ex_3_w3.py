import os
import zipfile

main_zip = zipfile.ZipFile('C:\\users\\Данила\\Downloads\\main.zip')
main_zip.extractall('C:\\cygwin64\\home\\Данила\\mipt_course_ap\\homework3')

with open('C:\\cygwin64\\home\\Данила\\mipt_course_ap\\homework3\\python_dirs.txt') as pd:
    list_of_dirs = []

    for cur_dir, dirs, files in os.walk('C:\\cygwin64\\home\\Данила\\mipt_course_ap\\homework3\\main'):
        for file in files:
            if file.endswith('.py') and cur_dir not in list_of_dirs:
                list_of_dirs.append(str(cur_dir))

    print(list_of_dirs)

    for i in range(len(list_of_dirs)):
        list_of_dirs[i] = list(map(str, list_of_dirs[i].split('\\')))
        list_of_dirs[i] = list_of_dirs[i][-1]
        print(list_of_dirs[i])

    list_of_dirs = map(lambda x: x + '\n', list_of_dirs)
    print(list_of_dirs)
    pd.writelines(list_of_dirs)
