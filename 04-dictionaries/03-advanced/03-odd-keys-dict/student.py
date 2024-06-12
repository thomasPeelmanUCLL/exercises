# Write your code here
def odd_keys_dict(dictionary):
    result = {}
    for k, v in dictionary.items():
        if k % 2 != 0:
            result[k] = v
    return result



def odd_keys_dict1(d):
    li=[]
    for key in range(len(d)):
        if d.items() % 2 == 0:
            del d[key]
        
    return d