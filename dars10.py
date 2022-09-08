# class Car:
#     def __init__(self,model,color,price,horsepower):
#         self.modeli = model
#         self.rangi = color
#         self.narxi = price
#         self.ot_kuchi = horsepower

#     def return_info(self):
#         return {
#             "model":self.model,
#             "color":self.color,
#             "price":self.price,
#             "horsepower":self.horsepower,
#             "capacity":self.capacity,
#             "weight":self.weight,
#         }    

# class Truck(Car):
#     def __init__(self,model,color,price,horsepower,capacity,weight):
     
#         self.hajmi = capacity
#         self.ogrligi = weight
#         super().__init__(self,model,color,price,horsepower,capacity,weight)
#     def show_info(self):
#         return {
#             "model":self.model,
#             "color":self.color,
#             "price":self.price,
#             "horsepower":self.horsepower,
#             "capacity":self.capacity,
#             "weight":self.weight,
#         }    

# ===============================================in copsulatsiya====================================================================#

class User:
    def __init__(self,name,surname):
        self.surname = surname
        self.name = name
    
    def __create_User(self):
        with open("users.txt","a") as fayl:
            fayl.write(self.surname+" "+self.name)

    def userCreate(self):
        self.__create_User()

class Student(User):
    def __init__(self, name, surname,group):
        User.__init__(self,name,surname)
        self.group = group
        
st1 = Student("Aziz","\nYaxyoyev","n60")
st1.userCreate()





