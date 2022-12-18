count = 0
range_count = 10
for_count = 0
run = True

while count < range_count:
    print("Hello Cycle Step=", count)
    if count == 3:
        print("Step =", count, "If body")
    count += 1 
    if count == range_count:
        print("Stop", count)

for item in range(for_count, range_count+1):
    print("Step =", item)
    
for item in range(0, 31):
    print("Step =", item)
    if item == 5:
        print("Item =", item)
    if item >= 27:
        print("Item >=", item)
        
for item in range(0, range_count+1):
    print("Step =", item)
    if item == 7:
        inner_count = 0
        print("-- inner_count =", inner_count)
        for inner_item in range(0, item):
            print("-------- Inner_Step =", inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print("-- inner_count =", inner_count)
        
for item in range(0, 20, 2):
    print("Step =", item)
    if item > 7 and item < 12:
        print("If_item =", item)
        continue
print("End_iteration =", item)

i = 1
n = 1
while i < 10:
    while n < 10:
        result = i * n
        print(result, end="\t")
        n += 1
    i += 1
    n = 1
    print("\n")


