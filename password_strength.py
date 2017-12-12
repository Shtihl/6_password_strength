import re
from getpass import getpass


def load_black_list():
    with open('./passwords.txt', 'r') as black_list_passwords:
        return black_list_passwords.read().splitlines()


def find_symbol_in_password(password):
    count_of_matches = 0
    for reg_exp in (r'\d',
                    r'[a-z]',
                    r'[A-Z]',
                    r'[~!@#$%^&*()_+`\-={}[\]:;<>./\\]'):
        if re.search(reg_exp, password):
            count_of_matches += 1
    return count_of_matches


def password_length(password):
    count_of_matches = 0
    unique_symbol_rate = 0.8
    if len(set(password)) > len(password) * unique_symbol_rate:
        count_of_matches += 3
    for length in [6, 12]:
        if len(password) >= length:
            count_of_matches += 1
    return count_of_matches


def get_password_strength(password, black_list):
    strength_points = 1
    if password in black_list or len(password) < 6:
        return strength_points
    else:
        strength_points = strength_points + \
                          password_length(password) + \
                          find_symbol_in_password(password)
        return strength_points


if __name__ == '__main__':
    user_password = getpass('Input your password: ')
    password_blacklist = load_black_list()
    strength_points = get_password_strength(user_password, password_blacklist)
    print('Your password strength is {} from 10'.format(strength_points))
