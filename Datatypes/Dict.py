#Dictionary {key : value}
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(dict1)
dict2 = {'pa':6, 'na':7, 'yi':8, 'nte':9, 'mone':10}
print(dict2)
print(dict2['pa'])
print(dict1['a'])

#sample

Bio = {
    "Name":"Alwin K G",
    "Age":21,
    "Qualification":"MCA",
    "Place":"Thrissur",
    "Post":"Python Fullstack Developer",
    "Mob no":9633529303,
    "Email":"alwinkgofficial@gmail.com"
}
print(Bio)
print(Bio['Name'])
print(Bio['Age'])
print(Bio['Qualification'])
print(Bio['Place'])
print(Bio['Post'])
print(Bio['Mob no'])
print(Bio['Email'])

Bio['Name']="AKG"
print("After updation our bio is: ",Bio)
Bio['Age']=20
print("After updation our bio is: ",Bio)

print(Bio.values())
print(Bio.keys())
print(Bio.items())
print(dict2.pop("mone"))
print(dict2.popitem())
print(dict2)
print(dict1.clear())
print(dict1)

del Bio['Qualification']
print("Deleting a key value pair using del operator:",Bio)

