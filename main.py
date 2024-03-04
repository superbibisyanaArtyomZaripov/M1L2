import time
import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890""+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pridumaypassword = int(input("какую длину пароля вы хотите?"))
generatedpassword = ""
for i in range(pridumaypassword):
    generatedpassword += random.choice(symbols)

print(generatedpassword)
