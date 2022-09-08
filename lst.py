list1 = [4,5,34,5,3,5,54,3,2]
list1 = set(list1) 
list1 = list(list1)

x = int(input('Son kiriting: '))
step = 0
for i in list1:
    step += 1
    for j in list1[step:]:
        if j+i==x:
            print(f'{i}+{j}={x}')
            break