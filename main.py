import re
path = input("Input the path of the file ")
file = open(path)
file_content = file.read()

regex = '["<>,\n!#$%&*()^\/]'
data = re.split(regex, file_content)
#print(data)

emails = '\w+@'
res = []
for names in data:
    temp = re.search(emails,names)
    if temp:
        res.append(names)

#print(res)
f = open("./emails.txt",'w')
for i in res:
    i = str(i)
    f.write(i.strip() + "\n")
f.close()
