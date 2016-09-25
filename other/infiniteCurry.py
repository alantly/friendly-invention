def add(a):
    def inner(*args):
        if len(args) == 0:
            return a
        return add(a + args[0])
    return inner

print add(1)(3)(5)()
