#funtion with no parameter
def hello_world_printer():
    print("hello world")


hello_world_printer()

#funtion with one parameter
def name_printer(enter_name):
    print(enter_name)

name = input("Enter your name ")

name_printer(name)

#volume of rectangular prism
#funtion with 3 params
length = int(input("Enter length in int: "))
width = int(input("Enter width in int: "))
height = int(input("Enter height in int: "))

def rect_volume(l,w,h):
    return l * w * h


print("The volume of the rectangular prism is "+str(rect_volume(length,width,height))+" cubic feet")


#celsius to fahrenheit
# F = 1.8*C+32

C = int(input("Enter an integer value "))

def fahrenheit(celsius):
    return round(1.8 * celsius + 32, 1)

print("The Fahrenheit equivalent of "+str(C)+" degrees Celsius is "+str(fahrenheit(C)))




