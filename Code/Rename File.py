import os

os.getcwd()
folder = "D:/Coding/Python/Project/rename-all-files/Test/"
num = 1
# listFile = []

for i, filename in enumerate(os.listdir(folder)):
    print(f'filename : {filename}')
    listFile = (filename.split('.'))
    oldName = listFile[0]
    extensionFile = listFile[1]
    # print(f'listFile : {listFile}')
    # print(f'Nama file : {listFile[0]}')
    # print(f'Ekstensi file : {listFile[1]}\n---------')

    newName = f"Wallpaper-{num}"
    newFilename = newName + '.' + extensionFile
    os.rename(folder + filename, folder + newFilename)
    print(f'newFilename : {newFilename}\n')
    num += 1


