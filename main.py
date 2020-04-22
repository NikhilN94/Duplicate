some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

temp = ''
duplicate =[]
length = len(some_list)

for _ in range(length):
  temp = some_list.pop()
  if temp in some_list:
    duplicate.append(temp)

print(list(set(duplicate)))