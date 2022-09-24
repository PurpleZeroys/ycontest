import math

profession = input('Введите название вакансии: ')
description = input('Введите описание вакансии: ')
years = int(input('Введите требуемый опыт работы (лет): '))
min_salary = int(input('Введите нижнюю границу оклада вакансии: '))
max_salary = int(input('Введите верхнюю границу оклада вакансии: '))
ske = input('Есть ли свободный график (да / нет): ')
premium = input('Является ли данная вакансия премиум-вакансией (да / нет): ')


def skl_time(years):
    if years == 1:
        print("Требуемый опыт работы:", years, "год")
    elif 2 <= years <= 4:
        print("Требуемый опыт работы:", years, "года")
    elif years <= 100:
        print("Требуемый опыт работы:", years, "лет")


def rounding(min_salary, max_salary):
    mid_salary = (max_salary + min_salary) / 2
    med_salary = math.floor(mid_salary)
    last_number = med_salary % 100
    if last_number == 1:
        print("Средний оклад:", med_salary, 'рубль')
    elif 2 <= last_number <= 4:
        print("Средний оклад:", med_salary, 'рубля')
    elif (4 < last_number <= 1000000) or last_number == 0:
        print("Средний оклад:", med_salary, 'рублей')


print(profession)
print("Описание:", description)
skl_time(years)
rounding(min_salary, max_salary)
print("Свободный график:", ske)
print("Премиум-вакансия:", premium)
   
