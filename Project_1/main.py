print("Hello automation")

for i in range(0,10):
    print('i = ', i)
    if i == 7:
        print('iii == ', i)

item = 88
name = 'Ilya'
result = str(item) +' '+ name

print(type(result))
print(result)

items = [item, name, 'Vadim', 33, [12, 28, "Hello"], {'age':30}, True, False, (0,1,3), 4.5]

print(len(items))
print(items[4][2])

dict_items = {'age':33,
              'name':"Ilya",
              'location': {'country': 'RB',
                           'city': 'Minsk'}}
print(type(dict_items), dict_items['location']['city'])
