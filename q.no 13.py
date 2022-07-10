input_string = input('Enter elements: ')
list1 = input_string.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
    if list1[i]%5==0:
        print(list1[i],end=" ")
