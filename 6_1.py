import re
list_1='afoot, catfoot, dogfoot, fanfoot, foody, foolery, foolish, fooster, footage, foothot, footle, footpad, footway, hotfoot, jawfoot, mafoo, nonfood, padfoot, prefool, sfoot, unfool'
list_2='Atlas, Aymoro, Iberic, Mahran, Ormazd, Silipan, altered, chandoo, crenel , crooked, fardo, folksy, forest, hebamic, idgah, manlike, marly, palazzo, sixfold, tarrock, unfold'

result_1=re.findall(r'\w*foo\w*',list_1)
result_2=re.findall(r'\w*foo\w*',list_2)
print('first list: ', result_1)
print('second list: ', result_2)

