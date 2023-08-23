dict_1 = {"1":"abs","2":"sdf","3":"erd","4":"wse","5":"qwe"}
print(dict_1)
print(dict_1["4"])
print('1' in dict_1)
print(2 not in dict_1)

dict_2 = {"Queen": "Bohemian Rhapsody", 
          "Bee Gees": "Stayin' Alive",
            "U2": "One", 
            "Michael Jackson": "Billie Jean", 
            "The Beatles": "Hey Jude",
              "Bob Dylan": "Like A Rolling Stone"
              }

print(len(dict_2))
for key in dict_2.keys():
    print(key)
print(dict_2.values())
for value in dict_2.values():
    print(value)
for key, value in dict_2.items():
    print(key, value)

print(dict_2.get("Promise of the Real","Not present"))

dict_3 = {}.fromkeys("bcd","consonant")

for key, value in dict_3.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}

popped = fast_food_items.pop("McDonald's")
print(popped)

fast_food_items.popitem()
print(fast_food_items)


internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
print(internet_celebrities)

cele = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(cele)

