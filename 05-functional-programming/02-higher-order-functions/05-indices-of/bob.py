def is_odd(x):
    return x % 2 != 0

def indices_of(xs, condition):
    return [x for x in xs if not condition(x)]

def test_indices_of():
    print(indices_of([1, 2, 3, 4, 5], is_odd))
    

test_indices_of()