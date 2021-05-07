l1 = [1,2,3,4,5,6] #dostepne monety
l3 = [1,5,6] #wydane monety


for el in l1:
    if el in l3:
        l1.remove(el)

print(l1)
