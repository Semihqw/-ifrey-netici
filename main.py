x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("lütfen parola uzunluğunu girin: "))
generated_password = ""
import random
for _ in range(password_length):
    generated_password += random.choice(x)
print("Oluşturulan parola:" , generated_password)