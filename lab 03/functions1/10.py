def uniques(elements):
    uniques = dict(())
    for element in elements:
        if(element not in uniques.keys()):
            uniques[elem] = 0
    return uniques.keys()
numbers = list(map(int, input().split()))
print(uniques(numbers))