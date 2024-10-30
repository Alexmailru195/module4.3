import re

def get_reg_data():
    reg_patterns = {
        'name': r'^[a-zA-Zа-яА-ЯёЁ]+$',
        'phone': r'^\+\d{1,3}\(\d{2,3}\)\d{7}$',
        'email': r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
    }
    return  reg_patterns

def check_unique_data(user_data, data_to_check):
    if user_data['phone'] in data_to_check['phones'] or user_data['email'] in data_to_check['emails']:
        return  False
    return True

def reg_check(user_data, reg_pattern, user_list, data_to_check=None):
    errors = []

    for field, pattern in reg_pattern.items():
        if not re.match(pattern, user_data[field]):
            errors.append(field)

    if not check_unique_data(user_data, data_to_check):
        errors.append('unique')

    if not errors:
        user_list.append(user_data)
        data_to_check['phones'].append(user_data['phone'])
        data_to_check['emails'].append(user_data['email'])

    return errors