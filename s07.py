name = 'Zelensky Volodymyr'

sp = name.index(' ')

sn = name[:sp]
fn = name[sp+1:]

name1 = fn + ' ' + sn
print(name1)

n1, n2 = name.split()
name2 = f'{n2} {n1}'
print(name2)