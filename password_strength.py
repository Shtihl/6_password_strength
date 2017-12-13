import re
from getpass import getpass
from string import punctuation


def load_black_list():
    with open('./passwords.txt', 'r') as forbidden_passwords_file:
        return forbidden_passwords_file.read().splitlines()


def find_pattern_in_password(password):
    count_of_pattern = 0
    reg_exps = [
        '\d',
        '[a-z]',
        '[A-Z]',
        '[{}]'.format(punctuation)
    ]
    for reg_exp in reg_exps:
        if re.search(reg_exp, password):
            count_of_pattern += 1
    return count_of_pattern


def password_length_points_count(password):
    password_length_points = 0
    min_acceptable_length = 6
    acceptable_length = 12
    length_limit = [
        min_acceptable_length,
        acceptable_length
    ]
    for length in length_limit:
        if len(password) >= length:
            password_length_points += 1
    return password_length_points


def password_uniqueness_check(password):
    password_uniqueness_points = 0
    unique_symbol_rate = 0.8
    if len(set(password)) > len(password) * unique_symbol_rate:
        password_uniqueness_points += 3
    return password_uniqueness_points


def get_password_strength(password, black_list):
    strength_points_result = 1
    min_acceptable_length = 6
    if password in black_list or len(password) < min_acceptable_length:
        return strength_points_result
    else:
        strength_points = [
            strength_points_result,
            password_length_points_count(password),
            find_pattern_in_password(password),
            password_uniqueness_check(password)
        ]
        strength_points_result = sum(strength_points)
        return strength_points_result


if __name__ == '__main__':
    user_password = getpass('Input your password: ')
    password_blacklist = load_black_list()
    strength_points_score = get_password_strength(
        user_password,
        password_blacklist
        )
    print('Your password strength is {} from 10'.format(strength_points_score))
