print("=========================")
print("PASSWORD STRENGTH CHECKER")
print("=========================")
paaswoed = input("Enter your password: ")
length = len(paaswoed)
print(length)
if length >= 12:
    print("strong password")
elif length >=8:
    print("medium password")
else:
    print("weak password")
