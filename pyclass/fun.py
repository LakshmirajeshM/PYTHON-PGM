#file = open("numbers.txt",'r')
#lines = file.readlines()
#print(lines)
#file.close()
file = open("numbers.txt", 'r')
lines= file.readlines()
for line in lines :
    if int(line)%2==0:
        print(line.strip())
file.close()

    

