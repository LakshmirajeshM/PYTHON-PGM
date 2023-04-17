x = input("enter your name :")
counter = {}

for i in x:
    if not i in counter:
        counter[i] = 1
    else:
        counter[i] = counter[i] + 1
print(counter)
most_occuring_letter = ""
max_so_far = 0
for i in counter :
    if counter[i]>=max_so_far:
        max_so_far = counter[i]
        most_occuring_letter = i
print(most_occuring_letter)
    
    