# Write your code here

def median(ns):
    ns.sort()
    if len(ns) % 2 == 0:
        mid = len(ns) // 2
        return (ns[mid - 1] + ns[mid]) / 2
    else:
        mid = len(ns) // 2
        return ns[mid]