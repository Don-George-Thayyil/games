def does_repeat(num,row):
    count = 0
    for i in row:
        if num == i:
            count += 1
    if count == 1:
        return True
    else:
        return False
#sample input
#195743862431865927876192543387459216612387495549216738763524189928671354254938671
#mess = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
mess = input("sequence for sudoku board: ")
mes = []
count = 0
for row in range(9):  #main array creation
    row = []
    #subrow = []
    #num = 0
    for column in range(9):
        row.append(mess[count])
        count+= 1        
    mes.append(row)

arr = []
finale = 0

for i in range(9):   #1st element array
    new_arr = []
    for j in range(9):
        new_arr.append(mes[j][i])
    arr.append(new_arr)

key = 0
sub = []
for i in range(3):  #sub array creation part 1
    subrow = []
    for row in mes:
        subrow.append(row[key])
        subrow.append(row[key+1])
        subrow.append(row[key+2])
    sub.append(subrow)
    key += 3

impkey = 0
finalsub = [[],[],[],[],[],[],[],[],[]]

for f in range(3):   #sub array creation part 2
    for j in range(1,28):
        if j%9 == 0:
            finalsub[impkey].append(sub[f][j-1])
            impkey += 1
        else:
            finalsub[impkey].append(sub[f][j-1])
           

for i in range(9):   #checking process
    for j in range(9):
        if does_repeat(mes[i][j],mes[i])and does_repeat(mes[i][j],arr[j]) and does_repeat(finalsub[i][j],finalsub[i]):
            finale += 1
        else:
            break


if finale == 81:
    print("No error in board sequence")
else:
    print("Found error in board sequence!!!")

