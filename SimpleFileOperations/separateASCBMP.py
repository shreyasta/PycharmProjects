import os
import shutil

#example of file name   base_path = 'S:\\MASTRecordings\\InfraRed Images\\NewS0812C_IR'

base_path = str(input('Please enter the path name:'))
a = os.chdir(base_path)
print(os.getcwd())

path_asc = os.path.join(base_path, 'PATH_ASC')
path_bmp = os.path.join(base_path, 'PATH_BMP')

os.makedirs(path_asc)
os.makedirs(path_bmp)

sourcefiles = os.listdir(base_path)

for file in sourcefiles:
    if file.endswith('.asc'):
        shutil.move(os.path.join(base_path, file), os.path.join(path_asc, file))

for file in sourcefiles:
    if file.endswith('.bmp'):
        shutil.move(os.path.join(base_path, file), os.path.join(path_bmp, file))