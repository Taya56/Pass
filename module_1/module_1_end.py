grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

for i in range(len(grades)):
    lst=sum(grades[i])/len(grades[i])

    students=list(students)
    
    average_score={}
        
    average_score[students[i]] = lst
    print(average_score)

# Это мой мозговой процесс.

# Мне надо узнать среднию оценку у значений в списке grades. Для того чтобы ускорить процесс, делаю это через for.
# Однако возникает проблема в бесконечном повторение цикла. Делаю ограничение до длины grades.
# Возникла проблема в том что у students и grades, разный тип данных, т.к. они не совместимы. Потому меняю тип данных у students, на список.
# Далее создаю переменую, словарь, в котором будут храниться все данные.

# Мне было трудно представить как можно было совместить список и множество в словарь потому я поискала как это впринципе делаеться.
# Ссылка на материал которым я воспользывалась https://translated.turbopages.org/proxy_u/en-ru.ru.1691d5b5-66d4302a-4044251c-74722d776562/https/www.geeksforgeeks.org/how-to-initialize-a-dictionary-in-python-using-for-loop
   
    





    




    
 
    




    
