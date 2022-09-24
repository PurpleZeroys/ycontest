import math

yes = "да"          #.,:;!_*-+()/#¤%&<>~`=\'\"@$№?qwertyuiopasdfghjklzxcvbnm
no = "нет"
profession, description, ske, premium, min_s, max_s, med_salary = 0, 0, 0, 0, 0, 0, 0
ske_bool = ""
premium_bool = ""
skl_year = ["год", "года", "лет"]
skl_money =['рубль', 'рубля', 'рублей']


def isdig(numbor):
    while numbor.isdigit() == False:
        print('Данные некорректны, повторите ввод')
        numbor = input('Введите требуемый опыт работы (лет): ')
    else:
        return numbor


def bool_rus(n):
    question = ['Есть ли свободный график (да / нет): ', 'Является ли данная вакансия премиум-вакансией (да / нет): ']
    questionParam = [ske, premium]
    questionParam[n] = input(question[n])
    while not ((questionParam[n] == yes) or (questionParam[n] == no)):
        print('Данные некорректны, повторите ввод')
        questionParam[n] = input(question[n])
        return questionParam[n]
    else:
        return questionParam[n]


def prof_nameordescr(n):
    questionParam = [profession, description]
    question = ['Введите название вакансии: ', 'Введите описание вакансии: ']
    use_char = ["йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ",
                "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM#()., "]
    enter = ['Введите название вакансии: ', 'Введите описание вакансии: ']
    questionParam[n] = input(question[n])
    while questionParam[n].isdigit() == True or questionParam[n].strip() == False \
            or any(char in use_char[n] for char in questionParam[n]) == False:
        print('Данные некорректны, повторите ввод')
        questionParam[n] = input(enter[n])
    else:
        return questionParam[n]


def salary_proof(n):
    salary = ['Введите нижнюю границу оклада вакансии: ', 'Введите верхнюю границу оклада вакансии: ']
    salaryParam = [min_s, max_s]
    salaryParam[n] = input(salary[n])
    while not salaryParam[n].isdigit():
        print('Данные некорректны, повторите ввод')
        salaryParam[n] = input(salary[n])
    else:
        salaryParam[n] = int(salaryParam[n])
        while salaryParam[n] < 0 or salaryParam[n] >= 4294967295:
            print('Данные некорректны, повторите ввод')
            salaryParam[n] = input(salary[n])
        else:
            return salaryParam[n]


profession = prof_nameordescr(0)
description = prof_nameordescr(1)
years = input('Введите требуемый опыт работы (лет): ')
years = isdig(years)
min_s = salary_proof(0)
max_s = salary_proof(1)
ske_bool = bool_rus(0)
premium_bool = bool_rus(1)


# def skl_time(years):
#     if years == 1:
#         print("Требуемый опыт работы:", years, "год")
#     elif 2 <= years <= 4:
#         print("Требуемый опыт работы:", years, "года")
#     elif years <= 4294967295:
#         print("Требуемый опыт работы:", years, "лет")



def rounding(min_salary, max_salary):
    mid_salary = (max_salary + min_salary) / 2
    med_salary = math.floor(mid_salary)
    return med_salary


def sklon(param, n, sklonenie):
    answer = ["Требуемый опыт работы:", "Средний оклад:"]
    param = int(param)
    if n == 1:
        last_number = param % 1000
    else:
        last_number = param

    if 1 == last_number:
        print(answer[n], param, sklonenie[0])
    elif 2 <= last_number <= 4:
        print(answer[n], param, sklonenie[1])
    elif (4 < last_number <= 4294967295) or last_number == 0:
        print(answer[n], param, sklonenie[2])



print(profession)
print("Описание:", description)
med_salary = rounding(min_s, max_s)
sklon(years, 0, skl_year)
sklon(med_salary, 1, skl_money)
print("Свободный график:", ske_bool)
print("Премиум-вакансия:", premium_bool)
