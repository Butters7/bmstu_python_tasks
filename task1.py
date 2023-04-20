import json

with open('vacs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Пункт 1. Не понял, что подразумевается под актуальными вакансиями

#Для пункта 2
vacancy_id = 0
vacancy_dict = {}

# Для 3 пункта
total_salary = 0
count_of_salary = 0

# Для 4 пункта
working_types = []

#Для 5 пункта
experience_min = 'без опыта'
total_salary_for_experience_min = 0
count_of_salary_for_experience_min = 0

#Для 6 пункта
experience_max = 'более 6 лет'
total_salary_for_experience_max = 0
count_of_salary_for_experience_max = 0

for vacancy in data:
    data = vacancy.get('data')

    work_type = data.get('working_type').get('title')
    salary_min = data.get('salary_min')

    if salary_min is not None:

        if data.get('currency').get('alias') == 'RUB':
            total_salary += salary_min
        else:
            total_salary += salary_min * 81.62
        count_of_salary += 1

        if data.get('experience_length').get('title') == experience_min:
            total_salary_for_experience_min += salary_min
            count_of_salary_for_experience_min += 1
        elif data.get('experience_length').get('title') == experience_max:
            total_salary_for_experience_max += salary_min
            count_of_salary_for_experience_max += 1


    if work_type not in working_types:
        working_types.append(work_type)


    salary_max_rub = data.get('salary_max_rub')
    if salary_max_rub is not None:
        vacancy_dict[vacancy_id] = [ salary_max_rub, vacancy ]
        vacancy_id += 1


working_types = ", ".join(working_types)
vacancy_dict = dict(sorted(vacancy_dict.items(), key=lambda x: x[1][0], reverse=True))


print(f'2) 10 вакансий с максимальной годовой заработной платы')
iter = 0
for vacancy in vacancy_dict:
    if iter == 10:
        break
    iter += 1
    print(vacancy_dict[vacancy][1])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'3) Средняя зарплата в рублях: {total_salary / count_of_salary:.2f} RUB')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'4) Все возможные типы занятости: {working_types}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'5) Число ваканский для старта карьеры: {count_of_salary_for_experience_min}. '
      f'Средняя зарплата в рублях: {total_salary_for_experience_min / count_of_salary_for_experience_min:.2f} RUB')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'6) Число ваканский с максимальным опытом: {count_of_salary_for_experience_max}. '
      f'Средняя зарплата в рублях: {total_salary_for_experience_max / count_of_salary_for_experience_max:.2f} RUB')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
