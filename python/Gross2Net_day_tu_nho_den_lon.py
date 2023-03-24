
s = input("Nhập lương Gross: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use numbers : ")
    check = s.isnumeric()
    if check == True:
        break

s = int(s)
p = input("Nhập số ng phụ thuộc: ")
check = p.isnumeric()
while check == False or int(p) < 0:
    p = input("Please,use numbers : ")
    check = p.isnumeric()
    if check == True:
        break

a = 11*10**6
p = int(p)
b = 4.4*10**6
print("giam_tru_gia_canh_ban_than ", a )
print("giam_tru_gia_canh_ng_phu_thuoc: ", p*b)

def luong_net(gross):
    net = 0
    bhxh = 0.08 * gross
    print("bao hiem xa hoi: ",bhxh)
    bhyt = 0.015 * gross
    print("bao hiem y te: ",bhyt)
    bhtn = 0.01 * gross
    print("bao hiem that nghiep: ",bhtn)
    sau_bao_hiem = gross - (0.08 + 0.015 + 0.01) * gross
    print("sau khi dong bao hiem thì con lai: ", sau_bao_hiem)
    net = 0
    if sau_bao_hiem <= (a + p*b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem)
        return net
    if sau_bao_hiem > (a+p*b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem-a-p*b)
        return net
def tien_dong_thue(chiu_thue):
    a = [5*10**6, 5*10**6, 8*10**6, 14*10**6, 20*10**6, 28*10**6]
    b = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    thue = 0
    for i in range(0,6):
        if chiu_thue <= a[i]:
            thue = thue + chiu_thue * b[i]
            chiu_thue = 0
            break
        else:
            thue = thue + a[i]*b[i]
            chiu_thue = chiu_thue - a[i]
    if chiu_thue > 0:
        thue = thue + chiu_thue * 0.35
    return thue

print("luong Net nhan dc la: ", luong_net(s))