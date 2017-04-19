import re

list_1='fu, tofu, snafu'
list_2='futz, fusillade, functional, discombobulated'

result_1=re.findall(r'\w*fu\b', list_1)
result_2=re.findall(r'\w*fu\b', list_2)

print('first list: ', result_1)
print('second list: ', result_2)
