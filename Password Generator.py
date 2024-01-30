import random
import string

lower_char_length = int(input("Enter no.of Lowercase Char "))
upper_char_length = int(input("Enter no.of Uppercase Char "))
digits_length = int(input("Enter no.of digits  "))
symbole_len = int(input("Enter no.of symbole "))

password_length = lower_char_length+upper_char_length+digits_length+symbole_len

lower =string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbole=string.punctuation2




str=random.choices(lower,k=lower_char_length)+random.choices(upper,k=lower_char_length)+random.choices(digit,k=lower_char_length)+random.choices(symbole,k=lower_char_length)
random.shuffle(str)
password="".join(str)
print("generator pasword is :",password)