from utils import get_reg_data, reg_check

users_list = []
data_to_check = {
    'phones': [],
    'emails': []
}

while len(users_list) < 3:
    user_data = {}
    reg_patterns = get_reg_data()

    filled_fields = 0

    for field in reg_patterns:
        value = input(f"Введите {field}: ")
        user_data[field] = value

    errors = reg_check(user_data, reg_patterns, users_list, data_to_check)

    if errors:
        print("Ошибки валидации:")
        for error in errors:
            if error == 'unique':
                print("Телефон или email не уникальны")
            else:
                print(f"Неккоректные значения в поле {error}")
    else:
        print("Данные валидны")

print("Добавлены следующие пользователи:")
for user in users_list:
    print(user)
