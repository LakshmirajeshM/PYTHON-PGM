file = open("numbers.txt", 'r')
lines= file.readlines()
file_to_write = open("even.txt",'w')
for line in lines :
    if int(line)%2==0:
        file_to_write.write(line.strip())
        file_to_write.write("\n")
file.close()
file_to_write.close()