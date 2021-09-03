
"""
Count letters in input strings
"""


def counter(word):

    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1

    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
    return count


sentence = input('>')
print(counter(sentence))
