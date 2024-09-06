# class my_calculator :
#     def product (self,*num ):
#         pro = 1
#         for x  in num:
#             pro = pro * x
#         print(pro)
#
# c1 = my_calculator()
# c1.product(4,5,6,7)
#

#
# class student :
#     callage_name = "seznas univercity"
#
#     def __init__(self,name,marks ):
#         self.names = name
#         self.mark = marks
#
#     def welcome (self) :
#         print("welcome student,",self.names)
#     def get_marks(self ):
#         return self.mark
#
# s1 = student("sezan",92)
# s1.welcome()
# print(s1.get_marks())
# print(student.callage_name)
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brak = False
#         self.clutch = False
#     def start (self):
#         self.clutch= True
#         self.brak= True
#         self.acc = True
#         print("the car is started ")
#
# car1 = car()
# car1.start()



# class Car :
#     @staticmethod
#     def start ():
#         print("car started ..")
#     @staticmethod
#     def stop():
#         print("car stopped..")
# class ToyotaCar (Car):
#     def __init__(self, name):
#         self.name = name
#
# car1 = ToyotaCar("fortuer")
# car2 = ToyotaCar("priso")
#
# print(car1 .start())
word = (" o")

# import random
#
# def guess_word(word):
#     while '_' in word:
#         guess = input("Guess a letter: ")
#         # Logic to update the word based on the guess
#         # ...
#     return word
#
# words = ["a", "b", "o"]
# word = "_" * len(random.choice(words))  # Initialize with underscores
#
# word = guess_word(word)
# print("You guessed the word:", word)

class student :
    def __init__(self,m ,a):
        self . m = m
        self . a = a
    def shownumber (self):
        print(self.m,"i +",self.a ,"j")

    def __add__ (self ,num2):
        newm = self.m + num2.m
        newa= self.a + num2.a
        return student(newm,newa)
num1=student(2,5)
num1.shownumber()
num2 = student(2,3)
num2.shownumber()

num3= num1 + num2
num3.shownumber()


