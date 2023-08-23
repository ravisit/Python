#Data types - numeric(integer,float,binary,octal), boolean(true,false) and #collection(string,list,tuple,set,dictionary)

#standard print stmt 

print("Hello world","Python course in August"); #it will print in same line.
print("Hello world","\tPython course in August"); #it will print in same line with xtra space.
print("Hello world","\nPython course in August"); #it will print in two line.

#Vaiable(can not start with number)

year = 2023;
_flp = 23.757280092; #variable can be start with '_' 
csname = "Python";   #variable can be lowercase
TRNAME = "Senthil";  #variable can be capital(all letters)

print("Hello users!! Welcome to", csname,"course. The Trainer is",TRNAME);

#Fancier print or modern 9day printing stmt

print(f"Hello users!! Welcome to the course:{csname} and the trainer is {TRNAME}");

#Printing along with precision

print('Hello, {0} the amt is {1:.2f} with count {2}'.format('Sam',2022.9865544,7822));
print('{0} Aligned Number with length {1} is: {2:>10}'.format('Right',10,34));
print('{0} Aligned Number with length {1} is: {2:<10}'.format('Left',10,34));

#Fancier print

print(f"The string used is {TRNAME} and the flp value is {flp:4.4f}");
print(f"The string used is {TRNAME:>11} and the flp value is {flp:4.4f}");

#inbuilt modules

import math;

r = round(math.pi,2);
print(r,math.trunc(math.pi),math.ceil(math.pi),math.floor(math.pi));

#use back slash for the escape sequence 

print(f"Hello Users!! \'Welcome\' \"Senthil\" 3\\4");

# Colored prints

print('\033[3;30;43m Vanakkam '+ 'Learners\n' + '\x1b[1;30;44m Colored values to show'+" Happy Learning\n")
print(f"\u001b[3;30;46m {b} and {a}");

print(f"The variable trname is {TRNAME} of the datatype : {type(TRNAME)}");

#type casting

s = str(int('123')+'cd');
print(fs,type(s));

#slicing

str1 = 'python course aug";
print(f"The length of strl is {len(str1)} and the slice st1[2:6:1] is {str1[2:6:1]}")
print(f"The slice of string str1[9:15] is {str1[9:19:3]}")
print(f"The slice of string str1[9:15] is {str1[:12:2]}")
print(f"The slice of string str1[9:15] is {str1[::2]}")
print(f"The slice of string str1[9:15] is {str1[::]}")
print(f"The slice of string str1[9:15] is {str1[16:3:-1]}")

#lower/upper
print(str1.upper())
print(str1.lower())

# 4. Sripping of spaces - strip(), lstrip(),rstrip()

rawinput = r'        This\t\n and That will Have \n\t

print(rawinput.rstrip())
print(rawinput.lstrip())
print(rawinput.strip())

#5. Captizaling or title case
print(rawinput.title())
print(rawinput.capitalize())

#4. Comparisions check for alpha numberic, aphbets, digits and lower,upper
print(csname.isalnum())
print(trname.isalpha())
print(csname.isdigit())
print(rawinput.isascii())
print(trname.lower().islower())
print(trname.lower().isupper())
#5. Finding or string pattern searching
s='That'
# find will give only the first occurance
print(f"The string {s} is print at {rawinput.find(s)}")

