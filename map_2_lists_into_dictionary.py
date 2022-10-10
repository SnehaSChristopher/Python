firstlist=[]
secondlist=[]
num=int(input("Enter no. of inputs: "))
for i in range(num):
    list_one=input("Enter as key: ")
    firstlist.append(list_one)
for i in range(num):
    second_list=input("Enter as value: ")
    secondlist.append(second_list)
dictionary = dict(zip(firstlist, secondlist))
print (dictionary)
