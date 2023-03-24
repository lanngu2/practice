ten_ng1 = input("nhap ten nguoi 1:")
tuoi_ng1 = input("nhap tuoi nguoi 1:")
dia_chi_ng1 = input("nhap dia chi ng 1: ")

ten_ng2 = input("nhap ten nguoi 2:")
tuoi_ng2 = input("nhap tuoi nguoi 2:")
dia_chi_ng2 = input("nhap dia chi ng 2: ")

ten_ng3 = input("nhap ten nguoi 3:")
tuoi_ng3 = input("nhap tuoi nguoi 3:")
dia_chi_ng3 = input("nhap dia chi ng 3: ")


def inng(name,age,adress):
    print("ten",name, age, "tuoi", "dia chi", adress);

inng(ten_ng1,tuoi_ng1,dia_chi_ng1)
inng(ten_ng2,tuoi_ng2,dia_chi_ng2)
inng(ten_ng3,tuoi_ng3, dia_chi_ng3)

def loainguoi(name,age,adress):
    age = int(age)
    tre_em = False
    if age < 20 or age == 20:
        tre_em = True

    if tre_em:
        print(name ,"la tre em")
    else:
        print(name," la nguoi lon")

loainguoi(ten_ng1,tuoi_ng1,dia_chi_ng1)
loainguoi(ten_ng2,tuoi_ng2,dia_chi_ng2)
loainguoi(ten_ng3,tuoi_ng3, dia_chi_ng3)