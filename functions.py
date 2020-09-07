def get_sum(one, two, delimiter='&'):
    a = str(one)
    b = str(two)
    return(a.upper() + delimiter + b.upper())

result = get_sum('Learn','python')
print(result)