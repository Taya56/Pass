#Словарь
my_dict = {"Tay": 2004, "Vlad": 2003}
print(my_dict)
print(my_dict["Tay"])
print(my_dict.get("tay"))
my_dict.update({"Kate":2004, "Vanya":2004})
pop=my_dict.pop("Kate")
print(pop)
print(my_dict)

#Множества
my_set = {1,2,3,4,"Привет", True, 1,2,3,4}
my_set.update({6,7})
my_set.discard(True)
print(my_set)