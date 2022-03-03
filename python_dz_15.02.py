'''
1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
    ```
    Андрей Говорухи               6  6  1  4  9  9  10 4  8  2  3  8
    Василий Петров                2  9  4  7  6  6  3  6  5  5  2  4
    Гавриил Варфаломеев           10 10 4  10 7  9  4  6  8  1  1  1
    Игнат Тюльпанов               8  1  4  1  1  5  2  5  2  2  10 8
    Илья Муромцев                 1  6  4  7  10 9  5  3  7  4  7  2
    Кощей Бессмертный             3  10 1  4  1  8  10 6  2  10 7  4
    Максим Мухин                  10 8  9  9  5  8  6  5  7  2  4  10
    Маргарита Мартынова           9  1  5  1  10 10 2  4  4  9  8  10
    Петр Николаев                 2  9  5  9  1  2  8  7  8  1  9  1
    Полина Гусева                 9  2  8  7  3  9  9  5  1  9  2  6
    Спиридов Тереньтьев           4  7  7  3  10 9  7  2  10 9  8  1
    Станислав Трердолобов         8  1  6  1  4  1  10 8  8  1  8  8
    ```
    Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
    записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":

    ```
    Говорухи А.         5.83
    Петров В.           4.92
    Варфаломеев Г.      5.92
    Тюльпанов И.        4.08
    Муромцев И.         5.42
    Бессмертный К.      5.5
    Мухин М.            6.92
    Мартынова М.        6.08
    Николаев П.         5.17
    Гусева Г.           5.83
    Тереньтьев С.       6.42
    Трердолобов С.      5.33
    ```

    Выравнивание колонок - желательно!
'''

import os


def func_students_names(students: str) -> list:
    with open(list_students, encoding= 'utf8') as f:
        lines = f.readlines()
        my_list = []
        text = ''
        for string1 in lines:
            for idx, word in enumerate(string1):
                if word.isalpha():
                    text += word
                elif word == ' ' and string1[idx+1].isalpha() and len(text) > 0:
                    text += word
        count = 0
        temporary = ''
        for idx, names in enumerate(text):
            if names == ' ' and count == 1 or idx == len(text) - 1:
                if idx == len(text) - 1:
                    my_list.append(temporary+text[-1])
                else:
                    my_list.append(temporary)
                    temporary = ''
                    count = 0
            elif names.isalpha():
                temporary += names
            elif names == ' ' and count == 0:
                temporary += names
                count += 1
        return my_list

def func_students_grades(students: str)-> list:
    with open(list_students, encoding= 'utf8') as f:
        lines = f.readlines()
        my_list = []
        text = ''
        for string1 in lines:
            for idx, num in enumerate(string1):
                if num.isdigit():
                    text += num
                elif num == ' ' and string1[idx+1].isdigit() and len(text) > 0:
                    text += num

        count = 0
        temporary = ''
        for idx, names in enumerate(text):
            if names == ' ' and count == 11 or idx == len(text) - 1:
                if idx == len(text) - 1:
                    my_list.append(temporary+text[-1])
                else:
                    my_list.append(temporary)
                    temporary = ''
                    count = 0
            elif names.isdigit():
                temporary += names
            elif names == ' ':
                temporary += ' '
                count += 1
        return my_list

def func_average_grade_of_each_student(grades: list) -> list:
    grade_list = []
    for num in students_grades:
        splited_num = num.split()
        number = 0
        count = 1
        for grade in splited_num:
            if count < len(splited_num):
                number += float(grade)
                count += 1
            elif count == len(splited_num):
                number += float(grade)
                number /= 12
                grade_list.append(round(number, 2))
    return grade_list

def func_students_average_grades_below_5(average_grade_of_students: list, students: list)-> str:
    students = ''
    for idx, below_5 in enumerate(average_grade_of_each_student):
        if below_5 < 5:
            students += students_names[idx] + '\n'
    return students

def func_average_all_grades(studets_grade: list, students: list) -> int:
    average_grades = 0
    for all_grades in average_grade_of_each_student:
        average_grades += all_grades
    average_grades /= len(average_grade_of_each_student)
    return round(average_grades, 2)

def func_of_str(names: list, grades: list) -> str:
    student_info = ''
    idx = 0
    for string in names:
        splited_string = string.split()
        student_info += (splited_string[1] + ' ' + string[0] + '.').ljust(15) + '{:>10}'.format(grades[idx]) + '\n'
        idx += 1
    return student_info

def func_create_doc(func_of_str: str) -> None:
    with open('students_grades.txt', 'w', encoding='utf8') as f:
        f.writelines(func_of_str)


if __name__ in '__main__':
    list_students = 'students.txt'
    students_names = func_students_names(list_students)
    students_grades = func_students_grades(list_students)
    average_grade_of_each_student = func_average_grade_of_each_student(students_grades)
    print(func_students_average_grades_below_5(average_grade_of_each_student, students_names))
    print('Средний балл по классу:', func_average_all_grades(average_grade_of_each_student, students_names))
    func_create_doc(func_of_str(students_names, average_grade_of_each_student))

########################################################################################################################


'''
Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
'''


def input_func():
    text = ''
    while True:
        user_input = input('Введите что-либо: ')
        if user_input == 'STOP':
            with open('user_input.txt', 'w', encoding='utf8') as f:
                f.writelines(text)
                print('End')
                break
        elif len(user_input) > 0:
            text += user_input + '\n'
            print('Что бы остановить программу введите STOP')

input_func()