import random 
insertOne = random.randint (3, 20)
insertTwo = []

def numbers_random(a,b):
    return list(range(a,b+1))

numbers_lst = numbers_random(1,insertOne)
couples_lst = []

for i in numbers_lst:
    for j in numbers_lst:
        sum = i+j
        if i == j:
            continue
        if sum <= insertOne:
            if insertOne % sum == 0:
                couples_lst.append([i,j])

def couples(couples_lst):
    unique_dict = []
    
    dict = {}
    for i in couples_lst:
        sorted_pair = sorted(i)
        tup = tuple(sorted_pair)
        if tup in dict:
            dict[tup] = False
        else:
            dict[tup] = True
    lst = list(dict)
    for i in lst:
        for j in i:
            unique_dict.append(j)
    numbers = "".join(map(str,unique_dict))
    return numbers
insertTwo = couples(couples_lst)

print(insertOne)
print(insertTwo)