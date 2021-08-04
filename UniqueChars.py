"""
check string has unique characters or not. if it contains duplicate char it returns False else return True
"""


def check_unique_chars(ip_str):
    count = {}

    for letter in ip_str:
        count[letter] = count.get(letter, 0) + 1

    if max(count.values()) > 1:
        return False
    else:
        return True


ip_string = "Welcome"

print(check_unique_chars(ip_string))
