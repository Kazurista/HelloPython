def myfunc(*args):
    x = 0
    new_string = ''
    while x < len(args)-1:
        if x%2 == 0:
            new_string + args[x].lower()
        else:
            new_string + args[x].upper()
            continue
        x += 1
    return new_string

myfunc('kazunari')
