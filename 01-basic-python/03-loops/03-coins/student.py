# Write your code here
def coins(one, two, five, goal):

    for i in range(five +1):
        for j in range(two +1):
            for k in range(one+1):
                if i*5 + j*2 + k == goal:
                    return True
    return False