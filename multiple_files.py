from utils import *
message = input("Please type your message\n")
fliped = flip(message)
counted = count_letters(message,"a")
print(f"Your encoded message is: {fliped}{counted}")