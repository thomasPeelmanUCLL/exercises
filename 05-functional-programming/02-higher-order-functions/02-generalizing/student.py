
def find_first_book_by_author(variables, condition):
    for var in variables:
        if condition(var):
            return var
    return None