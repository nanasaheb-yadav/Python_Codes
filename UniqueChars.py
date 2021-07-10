"""
check string has unique characters or not. if it contains duplicate char it returns False else return True
"""


def check_unique_chars(ip_str):
    count = {}

    for letter in ip_str:
        count[letter] = count.get(letter, 0) + 1

    for key, val in count.items():
        if val > 1:
            return False
        else:
            pass
    return True


ip_string = "Welcome"

print(check_unique_chars(ip_string))