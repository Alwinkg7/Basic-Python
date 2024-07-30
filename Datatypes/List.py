list1 = [1, 2, 'lala',3, 4, 5]
print("Print  the list: ",list1)
print(type(list1))
print(len(list1))

"""print(list1[2])
print(list1[-1])
print(list1[1:5])

for i in list1:
    print(i)

print(list1[0:5])
print(list1[1:4])
print(list1[2:3])"""
list2 = [9,8,'has',7]
print(list2)
#Using plus operator

list3 = list1+list2
print(list3)
list4 = [1,2,3,4,'python']
print(list4)
list4.insert(2,'alw',)
print(list4)
list4.remove('python')
print(list4)
list4.reverse()
print(list4)
list4.append(5)
list4.append('babi')
print(list4)
list4.copy()
print(list4)
list4.pop(2)
print(list4)
list4.clear()
print(list4)
list3.append(list1)
print(list3)
list2.extend(list1)
print(list2)
list1.remove('lala')
print(list1)
del list1[1]
print(list1)

