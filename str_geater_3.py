# #1.#write a program to check different validation check and accept use3r input if name is less than 3 show an error message and if greater than 50
# #show an error message 

# str=str(input("enter the name\n"))
# if (len(str)<=3):
#     print("invalid input,should be greater than 3")
# elif (len(str)>50):
#     print("the length should'nt be more than 50")
# else:
#     print("the name " ,str, "looks good")


# #2create a game of guessing the number ,give 3 chances of guessing the number

# import random
# num=random.randint(10,20)
# #print(num)

# for i in range(3):
#     x=int(input("enter the two number\n"))
#     if(x==num):
#         print("congrats you guessed the number ")
#     elif(x>=num):
#         print("the number is little lesser than wht you entered")
#     elif(x<=num):
#         print("the number is little bigger than you think")
#     else:
#         print("the entered number was" ,x )

# #write the code to show the car status as start or stop or exit 

# car = "idle"
# while True:
#     choice = str(
#         input("Enter either start/stop and type exit to exit the car: "))
#     if (car == "idle"):
#         if (choice.lower() == "start"):
#             print("Vroooooooooommmmmmmmmmmmmm")
#             car = "started"
#         elif (choice.lower() == "stop"):
#             print("Band gadi nahi rukti na")
#     elif (car == "started"):
#         if (choice.lower() == "start"):
#             print("Chalti gaadi ko kya start kar raha hai be")
#         elif (choice.lower() == "stop"):
#             print("Ceheeeeeeeeeeeeeeeeeeeeeeeeeeeee")
#             car = "idle"
#     if (choice.lower() == "exit"):
#         break


#     3. Write a generator function which takes an integer n as a parameter. The function should
# return a generator, which counts down from n to 0. Test your function using a for loop.

n=int(input("enter the number you want ot start countdown from"))
for i in range (n,1):
    
    print(i=i-1)