# Write your code here
def drop_nth(xs, n):
    return xs[:n] + xs[n+1:]

xs = [1, 2]
ys = [3, 4]

[xs, ys]     # == [[1, 2], [3, 4]]
[*xs, ys]    # == [1, 2, [3, 4]]
[xs, *ys]    # == [[1, 2], 3, 4]
[*xs, *ys]   # == [1, 2, 3, 4]