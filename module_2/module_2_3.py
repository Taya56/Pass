my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
lts=0

puss=[]

#До первого -числа

while True:
    if lts < len(my_list):
        if my_list[lts] < 0:
            break
        elif my_list[lts] > 0:
            print(my_list[lts])
        lts += 1
    else:
        break
print("Это конец")
