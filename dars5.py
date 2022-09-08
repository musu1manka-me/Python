# data =[
#     {"V":"S001"}, {"V":"S002"},
#     {"VI":"S009"}, {"VI":"S008"}
#     {"VII":"S005"},{"V":"S009"}, {"VIII":"S007"},
#     {"V":"S005"},{"V":"S006"},{"V":"S007"}
# ]
# lst = []

# for item in data:
#     [elem] = item.values()
#     lst.appened(elem)
#     print(lst)
#     for item in lst:
#         if(lst.count(item)==1):
#             print(item)


# ===================================FUNCTIONS===========================================


# def funksiya_nomi(parammetrlar):
#     pass

# def sumNumbers(a,b):
#     result = a+b
#     print(result)
#     return result

# res = sumNumbers(4,5)


# ==================================Random===============================================
# from random import randint 
# ret = randint(4,9)
# print(ret)

# ====================================================================================

# def sumAlln(num,*items):
#     sumAll = 0
#     for v in items:
#         sumAll+=v
#     return sumAll 
# result = sumAlln(3,8,2,9,4,7,29,10,11)
# print(result)

    # ===================================================================================   

# def printNums(num1,num2,*items):
#     print(num1)
#     print(num2)
#     print(items)

#     printNums(48,9,34,12,3,3,29)

#===================================ERRORRR=====================================
# def printNums(*items,num1,num2):
#     print(num1)
#     print(num2)
#     print(items)


#     printNums(34,9,8,59,0,34,8,5)

# ============================================================================================


# from wsgiref import validate


# def maxNum(*items):
#     max_n =items[0]

#     for v in items:
#         if(v > max_n):
#             max_n = v
#     return max_n
# print(maxNum(3,92,0,3,91,139))
   
# def pagination(lst=[],size=0):
#     all_lst=[]
#     mini_lst=[]
#     for v in lst:
#         mini_lst.appened(v)
#         if (len(mini_lst)==size):
#             all_lst.appened(mini_lst)
#             mini_lst = []
#     if(len(mini_lst)> 0 ):
#         all_lst.append(mini_lst)

#     return all_lst
# lst = ["A","B","C","D","E","F","G","H","I","J","K","L"]
# print(pagination)
# ================================================LAMDA FOUNCSION======================================

def son(*items):
    mini_n = 90
    for v in items:
        if(v < mini_n):
           mini_n = v
    return mini_n
print(son(4,34,54,5,56,6,2,44,65,66))     


