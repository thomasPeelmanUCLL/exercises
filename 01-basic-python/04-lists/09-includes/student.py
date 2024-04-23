# Write your code here
def includes(xs, ys):
    sortxs = sorted(xs)
    sortys = sorted(ys)
    for y in sortys:
        if y not in sortxs:
            return False
    return True