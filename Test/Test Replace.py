a = 'ini-adalah-file'
print(f'a : {a}\n')

aLists = a.split('-')
print(f'aLists : {aLists}\n')


for aList in aLists:
    aList+=aList
    aNew = aList


print(f'aList : {aList}\n')