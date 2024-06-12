def indices_of(xs, condition):
    return [x for x in range(len(xs)) if condition(xs[x])]

def indices_of1(xs, condition):
    return [index for index in range(len(xs)) if condition(xs[index])]