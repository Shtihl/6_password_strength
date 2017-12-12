import re
from getpass import getpass
from string import punctuation


def load_black_list():
    with open('./passwords.txt', 'r') as forbidden_passwords:
        return forbidden_passwords.read().splitlines()


def find_pattern_in_password(password):
    count_of_pattern = 0
    for reg_exp in ('\d',
                    '[a-z]',
                    '[A-Z]',
                    '[{}]'.format(punctuation)):
        if re.search(reg_exp, password):
            count_of_pattern += 1
    return count_of_pattern


def password_length_check(password):
    count_of_matches = 0
    length_limit = [6, 12]
    for length in length_limit:
        if len(password) >= length:
            count_of_matches += 1
    return count_of_matches


def password_uniqueness_check(password):
    password_uniqueness = 0
    unique_symbol_rate = 0.8
    if len(set(password)) > len(password) * unique_symbol_rate:
        password_uniqueness += 3
    return password_uniqueness


def get_password_strength(password, black_list):
    strength_points = 1
    if password in black_list or len(password) < 6:
        return strength_points
    else:
        strength_points = (strength_points +
                           password_length_check(password) +
                           find_pattern_in_password(password) +
                           password_uniqueness_check(password))
        return strength_points


if __name__ == '__main__':
    user_password = getpass('Input your password: ')
    password_blacklist = load_black_list()
    strength_points = get_password_strength(user_password, password_blacklist)
    print('Your password strength is {} from 10'.format(strength_points))
