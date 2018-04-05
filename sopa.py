column0=["A","B","C"]
column1=["D","E","F"]
column2=["G","H","I"]
column3=["J","K","L"]
soup=[column0,column1,column2,column3]
#comment
x=0
y=0

listStrings = []
#add columns
for i in range(len(soup)):
    listStrings.append(''.join(soup[i]))

print(listStrings)
#add rows

for i in range(len(soup)):
    column = soup[i]
    
    currentArray = []
    for j in range(len(column)):
        currentArray.append(soup[i][j])
    print(''.join(currentArray))
