txt = 'to be or NOT to be'

print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.capitalize())
print(txt.swapcase())

print(txt.startswith('t'), txt.endswith('t'))
print(txt.startswith('to'), txt.endswith('to'))
print(txt.startswith('be'), txt.endswith('be'))

print(txt.replace('be', 'beer'))


for c in 'b', 'c', ' ', 'x', 'o':
    if c in txt:
        n = txt.lower().count(c)
        p = txt.lower().find(c)
        print(f'\'{c}\' is in txt {n} times (pos={p})')
    else:
        print(f'\'{c}\' is not in txt')




# txt = txt.upper()
# print(txt)


