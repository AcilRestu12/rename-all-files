import re,string

# fullname = 'testing ke - $order files.png'
fullname = 'testing 2 ke-$order files.png'


listFile = fullname.split('.')
fileName = listFile[0]
extFile = listFile[1]

# dollar=re.sub('$([^\s]+)','',fileName)
num = 1
newName = fileName.replace('$order', str(num))

# for char in fileName:
#     print(f'char : {char}\n')
#     print(f'dollar : {dollar}\n')

print(f'listFile : {listFile}')
print(f'Nama file : {listFile[0]}')
print(f'Ekstensi file : {listFile[1]}\n---------')
print(f'newName : {newName}')
