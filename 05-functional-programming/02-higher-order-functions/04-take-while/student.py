def take_while1(xs, condition):
    result= []
    for x in xs:
        if condition(x):
            result.append(x)

        else:
            break
    return result 

def take_while(xs, condition):
    i = 0
    while i < len(xs) and condition(xs[i]):
        i += 1
    return (xs[:i], xs[i:])