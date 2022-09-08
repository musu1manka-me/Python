import random

lst = []

n = int(input("Nechta son bolsin: "))

for i in range(1,n+1):

    lst.append(random.randint(1,20))
print(lst)
print(max(lst))

