# STR

line = 'I love Python!'

# print(line)
# print(type(line))
# print(len(line))

# for idx in range(len(line)):
#     print(f'{idx} -> \'{line[idx]}\'')

# for ch in line:
#     print(ch)

for idx, ch in enumerate(line, start=1):
    print(idx, ch)

