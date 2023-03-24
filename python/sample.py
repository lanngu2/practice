
class Person: # là object là đối tượng
    def __init__(self, name, age, address):  # tên, tuổi, địa chỉ là Thuộc tính
        self.name = name
        self.age = int(age)
        self.address = address

    def loainguoi(self): # hàm ở trong class đc gọi là phương thức
        tre_em = False
        if self.age < 20 or self.age == 20:
            tre_em = True

        if tre_em:
            print(self.name ,"la tre em")
        else:
            print(self.name," la nguoi lon")
    def inng(self):
        print("ten", self.name, self.age, "tuoi", "dia chi", self.address)
num = 1
list_persons = []
while True:
    if num > 4:
        break
    ten_ng = input("nhap ten nguoi " + str(num) + ": " )
    tuoi_ng = input("nhap tuoi nguoi " + str(num) + ": ")
    dia_chi = input("nhap dia chi ng " + str(num) + ": ")
    tmp_p = Person(ten_ng, tuoi_ng, dia_chi)
    list_persons.append(tmp_p)
    num = num + 1

for person in list_persons:
    person.inng()
    person.loainguoi()

# p1 = Person("Person1", 36, "VN")
# p1.inng()
# p1.loainguoi()
# p2 = Person("Person2", 36, "VN")
# p2.inng()
# p2.loainguoi()
# p3 = Person("Person3", 36, "VN")
# p3.inng()
# p3.loainguoi()
# p4 = Person("Person4", 36, "VN")
# p4.inng()
# p4.loainguoi()
