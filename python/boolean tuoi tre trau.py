age = input("so tuoi cua ban: ")
age = int(age)

is_con_nit = False
if age < 10:
    is_con_nit = True

if is_con_nit:
    print("con nit")
elif age >= 15 and age <= 17:
    print("tre trau")
elif age == 18:
        print("sieu tre trau")
elif age > 18:
    print("nguoi lon")
else:
    print("sap tre trau")
