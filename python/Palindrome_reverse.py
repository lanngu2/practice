s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)

def palindrome(so):
    if so >= 0 and so <10:
        print(so, "la Palindrome")
    else:
        so = str(so)
        if so == so[::-1]:
            print(so,"la Palindrome")
        else:
            print(so, "KHong la Palindrome")

palindrome(s)