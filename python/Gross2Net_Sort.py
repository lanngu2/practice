#kiểu json hoặc dictionary, muốn xài theo thứ tự, bắt buộc phải dùng hàm sort
#e ko dùng thì khi test có thể đúng, nhưng khi chạy thực tế sẽ có lúc bị sai
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
    print("sau khi dong bao hiem thì con lai", sau_bao_hiem)
    net = 0
    if sau_bao_hiem <= (a + b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem)
        return net
    if sau_bao_hiem > (a+b):
        net = sau_bao_hiem - tien_dong_thue(sau_bao_hiem-a-b)
        return net
def tien_dong_thue(chiu_thue):
    a = {80*10**6: '0.35', 52*10**6: '0.3', 32*10**6: '0.25', 18*10**6: '0.2', 10*10**6: '0.15', 5*10**6: '0.1', 0: '0.05'}
#    sorted(a.keys())
    sorted(a.keys(), reverse=True)
    thue = 0
    for ai in a:
        while (chiu_thue - ai) > 0:
            print(ai)
            muc_nop_thue = (chiu_thue - ai) * float(a[ai])
            thue = muc_nop_thue + thue
            chiu_thue = ai
    return thue

print("luong Net nhan dc la: ", luong_net(s))