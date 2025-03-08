import file_operations


import os


import random


from faker import Faker


# Функция для замены символов
def apply_mapping(skill, mapping):
    return ''.join(mapping.get(char, char) for char in skill)


# Создаем экземпляр Faker с русской локалью
fake = Faker("ru_RU")

# Генерируем данные и сохраняем их в контексте
skills = ['Кислотный взгляд', 'Ледяной выстрел', 'Огненный заряд']

mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
 }

# Применение замен ко всем навыкам
modified_skills = [apply_mapping(skill, mapping) for skill in skills]
for i in range(10):
    context = {
    "first_name": fake.first_name(),  
    "last_name": fake.last_name(),
    "job": fake.job(), 
    "town": fake.city(),              
    "strength": random.randint(3, 18), 
    "agility": random.randint(3, 18),
    "endurance": random.randint(3, 18),
    "intelligence": random.randint(3, 18),
    "luck": random.randint(3, 18),
    "skill_1": random.sample(modified_skills,1),
    "skill_2": random.sample(modified_skills,1),
    "skill_3": random.sample(modified_skills,1),
    }

   # Создание имени выходного файла
    output_filename = f"charsheet-{i}.svg"
    output_path = os.path.join('output', output_filename)

    # Вызов функции для рендеринга шаблона
    file_operations.render_template("src/charsheet.svg", output_path, context)