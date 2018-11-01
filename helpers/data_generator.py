from random import choice


def get_random_string(length):
    source = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    res = ""
    for i in range(length):
        res += choice(source)
    return res
res = get_random_string(50)
print(res)


