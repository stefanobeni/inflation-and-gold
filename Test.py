p = 0

i = 1
for i in range(1, 6):
    print(i)
    p += i

print('p: ' + str(p))

list1 = range(9)
list2 = [n for n in list1 if n % 2 == 0]
print(list2)

#for i in range(3):
    #for j in range(3):
        #print('i: ' + str(i))
        #print('j: ' + str(j))
        #if i < j:
        #print('POPO')

print(5//2)

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
print(my_dict['apple'])
