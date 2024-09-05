print("Введите 3 целых числа:")
first=int(input())
second=int(input())
third=int(input())

if first==second==third:
    print("3 одинаковых числа")
elif first or second and third:
    print("2 одинаковых числа")
elif first and second or third:
    print("2 одинаковых числа")
else:
    print("Нет одинаковых чисел")
