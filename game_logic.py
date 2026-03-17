from response import *
from secret_number import *
secret_number = generate_secret_number()
user_input = ""
count = 0
while user_input != secret_number:
    user_input = int(input("What is your guess:"))
    input_response(secret_number,user_input)
    count += 1
    

print(f"It took you {count} tries!")