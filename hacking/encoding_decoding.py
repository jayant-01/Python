a = int(input("press 1 for encryption of data and 2 for decrypt it"))

if a == 1:
    s = input("enter the string to encrypt in ascii format")
    print(s.encode("ascii"))
elif a == 2:
    y = input("enter the ascii encrypted string")
    print(y.decode("ascii"))
else:
    print("you have made a wrong choice")
