print("write your firstname:", end=" ")
firstname = input()

print("write your lastname:", end=" ")
lastname = input()
print("your fullname is:" + firstname + " " + lastname)


import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
CURRENT_YEAR = now.year

year_born = input("when you were born: ")
x = year_born.isnumeric()

while x == False:
    year_born = input("Please,use numbers what date you were born: ")
    x = year_born.isnumeric()
    if x == True:
        break

year_born = int(year_born)
old = CURRENT_YEAR - year_born
if old >= 0 :
    # print("you are " + str(old) + " years old in "+ str(CURRENT_YEAR))
    print("you are {0} years old in {1}".format(old, CURRENT_YEAR))
else:
    print("Ban chua sinh ra")



