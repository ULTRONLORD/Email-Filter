lst = ['"',"'",';',"<",">",","," "]
path = input("Input the path of the file ")
file = open(path)
file_content = file.read()

new = file_content.split(lst[0])
newstr = ''
for i in new:
    newstr += i
#print(newstr)
new1 = newstr.split(lst[1])
new1str = ''
for i in new1:
    new1str += i
#print(new1str)
new2 = new1str.split(lst[2])
new2str = ''
for i in new2:
    new2str += i
#print(new2str)
new3 = new2str.split(lst[3])
new3str = ''
for i in new3:
    new3str += i
#print(new3str)
new4 = new3str.split(lst[4])
new4str = ''
for i in new4:
    new4str += i
#print(4)
#print(new4str)

nocomm = new4str.split(lst[5])
nocommstr = ''
for i in nocomm:
    nocommstr = nocommstr + i


#print("nocommstr")
#print(nocommstr)

fin = nocommstr.split("\n")
#print(fin[1])

final=[]
for i in fin:
    if i != '':
        final.append(i.lower())

#print(final)
comb = str(final[0])
#print(comb)
final.pop(0)
comblst = comb.split(" ")
#print(comblst)
for i in comblst:
    final.append(i)

print(final)

finish = []
for i in final:
    if "@" in i:
        finish.append(i)


f = open("./emails.txt", "w")
for i in finish:
    f.write(i + "\n")