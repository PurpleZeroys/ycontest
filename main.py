profession = input('Введите название вакансии: ')
description = input('Введите описание вакансии: ')
years = int(input('Введите требуемый опыт работы (лет): '))
min_salary = int(input('Введите нижнюю границу оклада вакансии: '))
max_salary = int(input('Введите верхнюю границу оклада вакансии: '))
ske = input('Есть ли свободный график (да / нет): ')
premium = input('Является ли данная вакансия премиум-вакансией (да / нет): ')
yes = "да"
no = "нет"


def funct(prov):
    if prov == yes:
        return True
    elif prov == no:
        return False


def types(anot):
    print(anot, ' (', type(anot).__name__, ')', sep='')


def bool_types(anotv2):
    print(funct(anotv2), ' (', type(funct(anotv2)).__name__, ')', sep='')


types(profession)
types(description)
types(years)
types(min_salary)
types(max_salary)
bool_types(ske)
bool_types(premium)