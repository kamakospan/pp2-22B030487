def f(l):

    x = []

    for a in l:

        if a not in x:

            x.append(a)

    return x

print(f([1,2,3,3,3,3,4,5]))