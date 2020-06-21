lang=['js','go','java','c']
print( len(lang))
print(lang[0])
# print(lang[-1])
# print(lang[0:2])
# print(lang[:2])
# lang.append('c#')
# lang.insert(2,'c#')
# print(lang)
# lang1=['js','php']
# # lang.insert(0,lang1)
# lang.extend(lang1)
# # lang.append(lang1)
# print(lang)
# print(len(lang))
# print(lang[0])
# lang.remove('js')
# popped= lang.pop()
# print(popped)
print(lang)
# lang.reverse()
no=[1,3,5,2,1,7,10]
lang.sort()
no.sort()
lang.sort(reverse=True)
no.sort(reverse=True)
# print(lang)
print(no)
slang= sorted(lang)
print(slang)
print(sum(no))
print(lang.index('js'))
print('c'in lang)

for ind,lan in enumerate(lang,start=1) :
  print(ind,lan)

lang_str=' - '.join(lang)
print(lang_str)
new_list=lang_str.split(' - ')
print(new_list)

# tuples
# list1=['maths','sci','geo','his']
# list2=list1
# print(list1)
# print(list2)
# list1[0]='phy'
# print(list1)
# print(list2)

# tuple1=('maths','sci','geo','his')
# tuple2=tuple1
# print(tuple1)
# print(tuple2)
# tuple1[0]='phy'
# print(tuple1)
# print(tuple2)

# sets
set1={'maths','sci','bio','his'}
set2={'chem','maths','bio','trio'}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
print('maths'in set1)


