# import os

# def countFiles(pathFile,file_count,dir_count):
#     for item in os.listdir(pathFile):
#         if(os.path.isfile(os.path.join(pathFile,item))):
#             file_count +=1
#         else:
#             dir_count+=1
#             [new_file_count,new_dir_count]= countFiles(os.path.join(pathFile,item),0,0)
#             file_count+=new_file_count
#             dir_count+=new_dir_count
#     return[file_count,dir_count]

# my_location = 'C:/Users/PC/Desktop/Bot' 
# #print(my_location)           
# print(countFiles(my_location,0,0))



# ==================================FILES=========================

# try:
#     fayl = open("new_text.txt","r")
#     reat = fayl.read()
#     print(reat)
# except:
#     print("Bunday file mavjud emas")
# # =================================================================    # 

# try:
#     fayl = open("new_text.txt","r")
#     try:
#         reat = fayl.read(1)
#         print(reat)
#     except:
#         print("Filedan oqishda qandaydir hatolik")    
# except:
#     print("Bunday file mavjud emas")

#  # ========================================================================

#     fayl = open("new_text.txt","r")
#     reat = fayl.readline(21)
# print(reat)
# # ===========================================================================

# fayl = open("new_text.txt","r")
# reat = fayl.readline(22)
# print(reat)