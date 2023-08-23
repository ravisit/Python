str_1 = input("Enter the string ")

reversed_str = ''

for letter in range(len(str_1)-1,-1,-1):
    reversed_str +=str_1[letter]

print(reversed_str)