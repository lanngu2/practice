
s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)


def palindrome(so):
    so = str(so)
    l = len(so)
    k = int(l/2)
    if so == 2 or so == 3 or so == 7 or so == 11:
        print(so, "la Palindrome")
    else:
        test = 1
        for i in range(0,k):
            if so[i] == so[l-i-1]:
                test = 1
            else:
                test = 0
                break
        if test == 1:
            print(so,"la Palindrome")
        else:
            print(so, "KHong la Palindrome")
if s == 1:
    print(s,"khong la nguyen to")
elif s == 2 or s == 3:
    print(s, "la so nguyen to")
else:
    import math
    k = int(math.sqrt(s))
    du = 1
    for i in range(2, k+1):
        du = s %i
        if du == 0:
            break
    if du == 0:
        print(s, "khong la so nguyen to")
    else:
        print(s,"la so nguyen to")
        palindrome(s)





