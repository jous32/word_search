#import pdb
#pdb.set_trace()
column0=["A","B","C"]
column1=["D","E","F"]
column2=["G","H","I"]
column3=["J","K","L"]
soup=[column0,column1,column2,column3]

listStrings = []
#add columns
print('0 for')
for i in range(len(soup)):
    listStrings.append(''.join(soup[i]))

#add rows
for j in range(len(soup[0])):
    currentArray = []
    for i in range(len(soup)):
        currentArray.append(soup[i][j])
    listStrings.append(''.join(currentArray))

# reverse strings
listStringsReversed = []
for s in listStrings:
    listStringsReversed.append(s[::-1])

#add reversed strings
for rs in listStringsReversed:
    listStrings.append(rs)

print(listStrings)
