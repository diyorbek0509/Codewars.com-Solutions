def spin_words(sentence):
    s = ""
    for i in sentence.split():
        if not s == "":
            s += " "
        if len(i) >= 5:
            s += i[::-1]
        else:
            s += i
    return s


print(spin_words("Hey fellow warriors"))  # result: Hey wollef sroirraw
