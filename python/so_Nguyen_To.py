s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)
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
            print(i)
            break
    if du == 0:
        print(s, "khong la so nguyen to")
    else:
        print(s,"la so nguyen to")
