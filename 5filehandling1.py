file = open("5filehandling1.txt",'r')
content = file.readlines()
file.close()

for i in content:
    print(len(i.strip()))
