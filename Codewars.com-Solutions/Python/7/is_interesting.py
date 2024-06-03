def is_interesting(number, awesome_phrases):
    if number < 100:
        return False
    else:
        if number//10**(len(str(number))-1) == int(str(number)[0]) or int(str(number + 1)[0]) == (number + 1)//10**(len(str(number + 1)) - 1) or (number - 1)//10**(len(str(number - 1)) - 1) == int(str((number - 1))[0]):
            return True, "shart - 1"
        if str(number).count(str(number)[0]) == len(str(number)):
            return True, "shart - 2"
    return False


print(is_interesting(121, []))
