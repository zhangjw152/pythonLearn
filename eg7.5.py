def say(message, num=1):
    print message * num


say('hello world')
say('bili', 10)


def hoho(a, b=3, c=20):
    return "a=", a, "b=", b, "c=", c


print hoho(2, 5, 6)
print hoho('d', c=345)
