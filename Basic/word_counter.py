exp = input("Enter a tring ")

def count_words(exp):
    spaces = 0
    for i in range(0,len(exp)):
        if(exp[i]==" "):
            spaces += 1
    return spaces+1

print(count_words(exp))

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

print(count_words(str_3))
print(count_words(str_2))
print(count_words(str_1))
