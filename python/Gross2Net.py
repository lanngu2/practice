s = input("Nhập lương Gross: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)
a = 11*10**6
b = 0
print("giam_tru_gia_canh_ban_than ", a )
print("giam_tru_gia_canh_ng_phu_thuoc" , b)


def luong_net(gross):
    net = 0
    bhxh = 0.08 * gross
    print("bao hiem xa hoi: ",bhxh)
    bhyt = 0.015 * gross
    print("bao hiem y te: ",bhyt)
    bhtn = 0.01 * gross
    print("bao hiem that nghiep: ",bhtn)
    sau_bao_hiem = gross - (0.08 + 0.015 + 0.01) * gross
    net = 0
    if sau_bao_hiem <= (a + b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem)
        return net
    if sau_bao_hiem > (a+b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem-a-b)
        return net
def tien_dong_thue(tien_chiu_thue):
    tiendongthue = 0
    if tien_chiu_thue <= 5*10**6 :
        tiendongthue = 0.05*tien_chiu_thue
        return tiendongthue
    if tien_chiu_thue > 5*10**6 and tien_chiu_thue <= 10*10**6:
        tiendongthue = 250000 + 0.1*(tien_chiu_thue-5*10**6)
        return tiendongthue
    if tien_chiu_thue > 10*10**6 and tien_chiu_thue <= 18*10**6:
        tiendongthue = 250000 + 500000+ 0.15*(tien_chiu_thue-10*10**6)
        return tiendongthue
    if tien_chiu_thue > 18*10**6 and tien_chiu_thue <= 32*10**6:
        tiendongthue = 750000 + 1.2*10**6+ 0.2*(tien_chiu_thue-18*10**6)
        return tiendongthue
    if tien_chiu_thue > 32*10**6 and tien_chiu_thue <= 52*10**6:
        tiendongthue = 750000+ (1.2 + 2.8)*10**6 + 0.25*(tien_chiu_thue-32*10**6)
        return tiendongthue
    if tien_chiu_thue > 52*10**6 and tien_chiu_thue <= 80*10**6:
        tiendongthue = 750000 + (1.2 + 2.8 + 5)*10**6+ 0.3*(tien_chiu_thue-52*10**6)
        return tiendongthue
    if tien_chiu_thue > 80*10**6 :
        tiendongthue = 750000 + (1.2 + 2.8 + 5+ 8.4)*10**6+ 0.35*(tien_chiu_thue-80*10**6)
        return tiendongthue
print("luong Net nhan dc la: ", luong_net(s))