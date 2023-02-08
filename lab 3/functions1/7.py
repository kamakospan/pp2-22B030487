def has_33(x):
    for i in range(len(x)-1):
        if x[i:i+2] == [3,3]:
            return True
    return False

x = list(input())