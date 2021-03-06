def makeBold(fn):
    def wrapper():
        return f"<b> {fn()} </b>"

    return wrapper


def makeItalic(fn):
    def wrapper():
        return f"<i> {fn()} </i>"
    return wrapper


@makeItalic
@makeBold
def input():
    return "Decorators code"

print(input())