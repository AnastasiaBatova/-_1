#Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students =(['Johnny','Bilbo','Khendrik','Steve', 'Aaron'])
#Упорядочить по алфавиту
list_of_students=['Johnny','Bilbo','Khendrik','Steve', 'Aaron']
print(sorted(list_of_students))
#Ищем средний балл
average_score={list_of_students[0]: float(sum(grades[0]))/float(len(grades[0]))}
print(average_score)
average_score1={list_of_students[1]: float(sum(grades[1]))/float(len(grades[1]))}
print(average_score1)
average_score2={list_of_students[2]: float(sum(grades[2]))/float(len(grades[2]))}
print(average_score2)
average_score3={list_of_students[3]: float(sum(grades[3]))/float(len(grades[3]))}
print(average_score3)
average_score4={list_of_students[4]: float(sum(grades[4]))/float(len(grades[4]))}
print(average_score4)
#Соотношение ученика с его средним баллом
list_of_students={"Aaron":average_score, "Bilbo":average_score1, "Johnny":average_score2,"Khendrik":average_score3,"Steve":average_score4}
print(list_of_students)


