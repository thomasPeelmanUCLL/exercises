# Write your code here
def target_sum(ns, target):
    ns.sort()
    i = 0
    j = len(ns) - 1
    while i < j:
        if ns[i] + ns[j] == target:
            return True