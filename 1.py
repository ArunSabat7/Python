#print hello msg
msg='Hello World modi'
# print(msg)
# print(len(msg) )
# print(msg.lower())
# print(msg.upper())
# print(msg[6:])
# print(msg.count('o'))
# print(msg.find('Hello'))
msg= msg.replace('World','Universe')
print(msg)
greeting='hello'
name='shah'
m=greeting+', '+ name
m='{} {}. welcome'.format(greeting,name)
m=f'{greeting} {name.upper()}. welcome' #alternate of line 15
print(m)
# print(dir(name))
# print(help(str))
print(help(str.lower))
