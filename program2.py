#This program will ask the user their name as well as their dream job and print the data in a fancy way
#Thea P. Uy
#March 16, 2024

import colorama
colorama.init(autoreset=True)
import pyfiglet

#define the variables
name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")
greetings_to_user = ("Hey,")
message_to_user = ("You are gonna be")
closing_message = ("Believe it !!")

#define the font of the message and the input
greetings_to_user = (pyfiglet.figlet_format(greetings_to_user,font='banner3'))
name = (pyfiglet.figlet_format(name,font='banner3-D'))
message_to_user= (pyfiglet.figlet_format(message_to_user,font='banner3'))
dream_job = (pyfiglet.figlet_format(dream_job,font='banner3-D'))
closing_message = (pyfiglet.figlet_format(closing_message,font='banner3'))

#define the color of the message and the input
greetings_to_user = (colorama.Fore.WHITE + greetings_to_user)
name = (colorama.Fore.YELLOW + name)
message_to_user = (colorama.Fore.WHITE + message_to_user)
dream_job = (colorama.Fore.YELLOW + dream_job)
closing_message = (colorama.Fore.BLACK + closing_message)

#print all the messages and the input
print(greetings_to_user)
print(name)
print(message_to_user)
print(dream_job)
print(closing_message)

#This is the end of the program
#Thank You