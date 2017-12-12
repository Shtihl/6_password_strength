import re
from getpass import getpass


def load_black_list():
    with open('./passwords.txt', 'r') as black_list_passwords:
        return black_list_passwords.read().splitlines()


def get_password_strength(password, black_list):
    strength_points = 1
    unique_symbol_rate = 0.8
    if password in black_list or len(password) < 6:
        return strength_points
    if len(set(password)) > len(password) * unique_symbol_rate:
        strength_points += 2
    if re.search(r"\d", password):
        strength_points += 1
    if re.search(r"[a-z]", password):
        strength_points += 1
    if re.search(r"[A-Z]", password):
        strength_points += 1
    if re.search(r"[~!@#$%^&*()_+`\-={}[\]:;<>./\\]", password):
        strength_points += 2
    length_list = [6, 10]
    for length in length_list:
        if len(password) >= length:
            strength_points += 1
    return strength_points


if __name__ == '__main__':
    user_password = getpass('Input your password: ')
    password_blacklist = load_black_list()
    strength_points = get_password_strength(user_password, password_blacklist)
    print('Your password strength is {} from 10'.format(strength_points))
