#RANGE

#list = [1,2,3]

#for item in list:
 #   print(item)

print("///////////////////")

for item in range(10):
    print(item)

print("///////////////////")

for item in range(5, 10): #5 ten başlasın 10a kadar gitmesi için
    print(item)

print("///////////////////")

for item in range(50,100,10): #50den başlasın 100 e kadar 10ar 10ar gitmesi için
    print(item)

print(list(range(5,100,10)))


#ENUMERATE

index = 0
greeting = 'hello'

for letter in greeting:
    print(f'index: {index} letter: {greeting[index]}')
    index +=1

print("//////////////////////")

greeting = 'hello'

for item in enumerate(greeting):
    print(item)

print("//////////////////////")

greeting = 'hello'
for index, item in enumerate(greeting):
    print(f'index: {index} letter:  {item}')

#ZIP - listeleri birbirleri ile eşleştirmek için kullenılır.
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip (list1,list2, list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

