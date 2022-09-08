# def shifrlaw(word):
#     for v in word:
#         if(v.islower()):
#             print(chr(122-(ord(v)-97)),end="")
#         elif(v.isupper()):
#             print(chr(90-(ord(v)-65)),end="")

# shifrlaw('sarvar') #output: hziezi


# def find_near(lst,number):
#     new_lst = []
#     min_value = abs(number - lst[0])

#     for v in lst:
#         if(abs(number-v)<min_value):
#             min_value = abs(number-v)

#     for v in lst:
#         if(abs(number-v)==min_value):
#             new_lst.append(v)        
#     return new_lst        

# lst = [34,56,2,32,4,6,46,3,6,5,3,5] 
# print(find_near(lst,50))   



# def Tekwr(number,lst):
#     pass




# lst = [
#     [2,3,1,6,3,1,0],
#     [3,4,2,7,4,2,3],
#     [7,6,7,8,5,3,6],
#     [9,7,8,9,6,4,7],

# ]


# ========================================================================================


# def AdvancedSort(lst):
#     new_lst = []





# lst = [80,70,80,60,80,70] 

# ============================ OOP misollar==================================================


# class Computer:
#     def __init__(self,nomi,RAMI,Narxi,protsessor):
#         self.nomi = nomi
#         self.RAMI = RAMI
#         self.narxi = Narxi
#         self.protsessori = protsessor
       
#     def showInfo(self):
#         print(f"""
#         Nomi:{self.nomi}
#         RAMI:{self.RAMI}
#         Narxi{self.narxi}
#         Protsessori:{self.protsessori}
#         """)

# computer1 = Computer("ASUS X515",8,"10.000$","Intel(R)")    
# computer2 = Computer("Apple",4,"9.000$","Intel(A)") 
# computer3 = Computer("HP",6,"5.000$","Intel(I)") 
# computer4 = Computer("ACER",3,"5.000$","Intel(B)") 

# all_computers = [computer1,computer2,computer3,computer4]


# for comp in all_computers:
#     if(comp.RAMI > 4 and comp.RAMI < 16):
#         comp.showInfo()
#         print("==================================================")























