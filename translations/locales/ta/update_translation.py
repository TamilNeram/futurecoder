import csv
import polib
po = polib.pofile("futurecoder_Tamil.po")


with open ("futurecoder_Tamil.csv" , mode = 'r') as file:
    csvFile = csv.reader(file)
    c1=[]
    c2=[]
    for lines in csvFile:
        c1.append(lines[0])
        c2.append(lines[1])

count = 0
for entry in po:
    if entry.msgstr == "":
        try:
            row_no=c1.index(entry.msgid)
            count += 1
            entry.msgstr=c2[row_no]
        except ValueError:
            print(entry.msgid +" Not Found")
         
print(count)
    
po.save("futurecode_TaFull.po")
