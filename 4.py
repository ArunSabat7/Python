# dictionary
stu={'name':'modi','age':56,'lan':['js','go','java']}
stu['phone']=8644748
stu['name']='shah'
stu.update({'name':'raj','age':64,'phone':453214997})
# del stu['name']
print(len(stu))
print(stu.keys())
print(stu.values())
print(stu.items())
print(stu['lan'])
print(stu)
print(stu.get('phone','not found'))

for keys,values in stu.items():
 print(keys,values)
