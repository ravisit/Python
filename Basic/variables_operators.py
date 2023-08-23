num = 5
float_1 = 6.987
bool_1 = True
string_1 = 'Char'

#operators Math

sum = num + float_1
subtraction = float_1 - num
multi = num * float_1
exponential = num ** 3
division = 56 / num
floor_division = 56 // num
modulus = 56 % num


#expresssion and precedence order

# Expression: (9-7)*2 **  3 +10 % 6 // -1 *2 -1
#step 1 : 2 * 2 ** 3 +10 %6 // -1 *2 -1  --- () first execute
#step 2 : 2 * 8 + 10 % 6 // -1 * 2 - 1 ---exponential(**) excute
#step 3 : 16 + -8 - 1 ---- *,//,% has same precedence so ltr
#step 4 : 7 ---- +,- has same precedence so ltr

print((9-7)*2 **  3 +10 % 6 // -1 *2 -1) #ans 7


