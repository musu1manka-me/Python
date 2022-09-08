#"================================================================================="

# x = 4.5
# y = 4.5
# print(x is y)  #ikkita qiymat ozaro tengligini tekshiradi

#"=================================================================================="

# word = "bugun dars kech boshlandi"
# let = "q"
# print(let in word) #kiritilgan belgi yoki soz(harf,son) ikkinchi satrda bor yoqligni tekshiradi

#"=================================================================================="

# word = "salom aka"
# let = "akam"
# print(let[0:3]in word)

#"=================================================================================="

# print(4>2 and 5>1)
# print(4>2 and (5>1 or 6>9)and 9<0)

#"=================================================================================="

#print("b">"a")

#"======================================IF ELSE====================================="

# son = int(input("son kirit: "))

# if(son==0):
#     print("nol")
# elif(son==1):
#     print("bir")
# else:
#     print(f"bu {son} soni")

    #"=================================================================================="

    # son = int(input("son1: "))
    # son2 = int(input("son2: "))
    # if(son%2==0 and son2%2==0):
    #     print("ikkalasiyam juft")
    # elif(son%2!=0 and (son2%2!=0)):
    #     print("Ikkalasiyam toq")
    
    #"=================================================================================="

# son = int(input("Son kirit: "))

# if(son%3==0 and son%5==0 ):
#     print("FIZZBUZZ")
# elif(son%3==0):
#     print("FIZZ")
# elif(son%5==0):
#     print("BUZZ")
# else:
#     print("Boshqa son kirit")

#"=================================================================================="

word = "dudhuidhwuqidhcisaohiduecxce"
counter  = 0
while counter<len(word):
    if word.count(word[counter])==1:
        print(word)
    counter+=1