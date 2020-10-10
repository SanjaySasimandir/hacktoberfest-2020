line=list(input())
count=0
for letter in line:
    if letter.islower():
        count+=ord(letter)-96
    else:
        count+=ord(letter)-64
print(count)
