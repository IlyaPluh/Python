#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
l = [1, 2, 3]
a = 'abc'
l.extend(a)
# l+=a
print(l)

# 3. Все чётные числа вывести в другой список
l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
print([result for result in l if result % 2 == 0])

# 4. Все emails у которых есть слово test вывести в другой список
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]
k=[]
for i in l:
     if 'test' in i:
          k.append(i)
print(k)


# 5. Найти самое маленькое число в списке
l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]
print(min(l))

# 6. Сравнить 2 строки без учёта регистра
str1 = 'IlyA'
str2 = 'iLYa'
print(str1.lower() == str2.lower())


# 7. Проверить является ли массив подмножеством другого массива
l1 = [5,6,6,1]
l2 = [9,5,1,10,4,33,2,6,8]
l1.sort()
l2.sort()
c = 0
p = 0
for i in l1:
     for j in range(p, len(l2)):
          if i == l2[j]:
               c += 1
               p = j+1
               break       
print(c == len(l1))

# 8. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.
str = 'attachment'
abc = 'qwertyuiopasdfghjklzxcvbnm'
for i in abc:
     c = 0
     for j in str:
          if j==i:
               c+=1
     if c >= 2:
          print(i, 'est', c, 'raz')
          
def foo(string):
     abc = 'qwertyuiopasdfghjklzxcvbnm'
     return {i: string.count(i) for i in abc if string.count(i) > 1}
print(foo('attachment'))

# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.
# no_duplicate_letters("Здравствуйте, Александра") ➞ False
# Две в в «Здравствуйте», три a в «Александра».
# no_duplicate_letters("Всегда дожимай до конца") ➞ True
# Две в в «Здравствуйте», три a в «Александра».
def foo(string):
     return len(set(string)) == len(string)
print(foo('test'))
print(foo('tes'))

#10. Напишите функцию, которая проверяет сложность пароля. Функция проверяет ряд условий и оценивает сложность пароля. 
# За каждое выполненое условие пароль получает бал.
# Если выполняется одно условие - функция возвращает 1, если выполненяется 5 условий - функция вернет 5.
# Условия которые нужно проверить:
# длина пароля не меньше 6 символов,
# пароль содержит хотя бы 1 цифру,
# пароль содержит хотя бы одну заглавную букву,
# пароль содержит хотя бы одну строчную букву,
# пароль содержит хотя бы один из специальных символов: !@#$%^&*()-+
# Типы символов, которые будут содержаться в пароле во время тестирования:
# Пароль не должен содержать кириллических символов
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def check(string):
     count = 0
     if len(string) >= 6:
          count += 1
     if (next((el for el in string if el in numbers), 'Not')) != 'Not':
          count+=1
     if (next((el for el in string if el in upper_case), 'Not')) != 'Not':
          count+=1
     if (next((el for el in string if el in lower_case), 'Not')) != 'Not':
          count+=1
     if (next((el for el in string if el in special_characters), 'Not')) != 'Not':
          count+=1     
     return(count)
print(check('23aS@jGG44'))
print(check('aS@jGG'))
print(check('aS'))
