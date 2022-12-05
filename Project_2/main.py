stroka = "Ilya"
integer = 33
flo = float(integer)
byte = bytes(integer)
list = ["apple", "banana", "cherry"]
tuple = ("cherry", "banana", "apple")
set = {"banana", "cherry", "apple"}
froze = frozenset(list)
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(stroka), stroka, type(integer), integer, type(flo), flo, type(byte), byte,
      type(list), list, type(tuple), tuple, type(set), set, type(froze), froze, type(dict), dict)

name = "Ilya"
nick = "Pluha"
nickname = name + nick
print(nickname)

print(stroka + ",", integer)
print(stroka + " " + str(integer))
