grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Работа над ошибками

#Преподаватель сказал:" Вам осталось отсортировать методом sorted весь ваш список студентов."
    #Узнала, как работает sorted и sort.
#Еще 1-а ошибка: У меня, за приделами цикла for, выводится только часть списка - что является ошибкой, как я позже узнала.
    #Что бы это исправить выношу average_score, за пределы цикла.
#Ошибка 2:  строка <students=list(students)>, заменяется на <students=sorted(students)>

average_score={}
      
for i in range(len(grades)):
    lst=sum(grades[i])/len(grades)     
    students=sorted(students)
    average_score[students[i]] = lst
print(average_score)

