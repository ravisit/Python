sample_list = [1,2.3,True,'ravi',[1,2,3]]
sample_list_1 = list('ravi')
print('e' in sample_list_1)
print('a' not in sample_list)
print('a' not in sample_list_1)

list_1 = [[0,2],[4,6],[8,10],[12,14]]
print(list_1[0])
print(list_1[3][1]) #accessing

list_2 = ["chair", "table", "desk", "lamp", "bed"]
print(list_2[-5])
print("Most people own at least "+str(list_1[0][1])+" "+str(list_2[-5])+"s.")
list_3 = [0.98, 8.76, 6.54, 4.32]
print(list_3[1:])
print(list_3[1:3])
print(list_3[:2]) #slicing

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals)
arctic_animals.remove("elephant")
print(arctic_animals)
arctic_animals.append("arctic fox")
print(arctic_animals)
arctic_animals.insert(3,"snowy owl")
print(arctic_animals)
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())


