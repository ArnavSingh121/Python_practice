import random

print("password generator")

user_input = int(input(' How long does your password need to be >> '))

pass_str = "ABCDEFGHIJKLBNOPQRSTUVWXYZ0123456789!@#$%^&*()"

password = ''.join(random.choices(pass_str, k = user_input))

print('Your password is >>', password)