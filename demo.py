# # a=2
# # b=3
# # c=a*b
# # print(c)


# print("hello Prakhar!!!")



#print(5*8/2+6-2)

# PRAKHAR =25
# print(PRAKHAR * 5)

# True
#Falsess

# name = input("what is your name ?")
# print("Hello " + name+ "!")

# age= int(input("enter your age"))
# print(age)

# def request_age():
#     age=input("enter your age")
#     return int(age)

# user_age = request_age()

# demo.py

# def request_age():
#     age = ''
#     while age.isdigit() == False :
#      age = input("Enter your age: ")
#      if age.isdigit() == False:
#         print("Enter a valid age")
#     return int(age)

# # Call the function
# user_age = request_age()
# print(f"You are {user_age} years old!")

def play_again():
    """this is a programe which takes y or n as an input"""
    answer = ''

    while answer.lower() not in ["y", 'n']:
        answer = input("do you want to play again? : ")

        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Enter Y or N only. please try again")

# call the function
# play_again()
# print(play_again__doc__)
# type(play_again)


def welcome():
    message = 'welcome to the world of python!!'
    hello = message.upper()
    print(hello)

# welcome()



def play_again(answer):
    if answer == 'yes':
        return True
    else:
        return False
