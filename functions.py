def get_summ(one, two, delimiter='&'):
    a = str(one)
    b = str(two)
    return(a.upper() + delimiter + b.upper())

result = get_summ('Learn','python')
print(result)