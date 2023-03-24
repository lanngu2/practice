mot_chuso = {0: '', 1: 'mot', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
mot_chuso_tu =  {0: '', 1: 'mot', 2: 'hai', 3: 'ba', 4: 'tu', 5: 'lam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
hang_chuc = {0: '', 1: 'muoi ', 2: 'hai muoi ', 3: 'ba muoi ', 4: 'bon muoi ', 5: 'nam muoi ', \
            6: 'sau muoi ', 7: 'bay muoi ', 8: 'tam muoi ', 9: 'chin muoi '}
hang_tram = {0: '', 1: 'mot tram ', 2: 'hai tram ', 3: 'ba tram ', 4: 'bon tram ', 5: 'nam tram ', \
            6: 'sau tram ', 7: 'bay tram ', 8: 'tam tram ', 9: 'chin tram '}
hang = {0: '', 1: 'nghin', 2: 'trieu', 3: 'ti', 4: 'nghin ti', 5: 'trieu ti', \
            6: 'ti ti', 7: 'nghin ti ti', 8: 'trieu ti ti', 9: 'ti ti ti'}
s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)
def doc(so):
    k = len(str(so))
    if k == 1:
        print(mot_chuso[so], end=" ")  # print, inte att använda return
    if k == 2:
        return hai_chuso(so)
    if k == 3:
        return ba_chuso(so)
def hai_chuso(ab):
    if ab == 11:
        print("muoi mot", end=" ")
        return "muoi mot"
    elif ab == 14:
        print("muoi bon", end=" ")
        return "muoi bon"
    elif ab == 44:
        print("bon muoi bon", end=" ")
        return "bon muoi bon"
    else:
        b = int(ab)//10
        d = ab - b*10
        print(hang_chuc[b] + mot_chuso_tu[d], end=" ")
        return hang_chuc[b] + mot_chuso_tu[d]
def ba_chuso(abc):
    du_chuc = abc - (abc//100)*100
    so_chuc = du_chuc//10
    doc_ba = []
    if so_chuc == 0 and (abc%100)%10 != 0:
        print(hang_tram[abc//100] + "linh " + mot_chuso[(abc%100)%10])
        doc_ba.append(hang_tram[abc//100] + "linh " + mot_chuso[(abc%100)%10])
    else:
        print(hang_tram[abc//100])
        doc_ba.append(hang_tram[abc//100])
        doc_ba.append(hai_chuso(int(du_chuc)))
#    print(type(doc_ba))   k the in ra dc cai list nay, mặc dù báo là list
    print(doc_ba)
    return doc_ba

def doc_so(abcd):
    if abcd >= 0 and abcd < 1000:
        return doc(abcd)
    if abcd >= 1000:
        return so_lon(abcd)
def so_lon(a):
    cach_doc = []
    a = list(str(a))
    l = len(a)
    z = l // 3
    d = l % 3
    if d == 1:
        a0 = int(a[0])
        cach_doc.append(doc(a0))  # k the dung + print(hang[z]))
        print(hang[z])
        cach_doc.append(hang[z])
    if d == 2:
        a12 = a[0:2]
        doi_a12 = [str(i) for i in a12]
        so_a12 = "".join(doi_a12)
        so_a12 = int(so_a12)
        cach_doc.append(doc(so_a12))  # k the dung + print(hang[z]))
        print(hang[z])
        cach_doc.append(hang[z])
    for i in range(0, (z-1)):
        ai = a[(l - 3 * (z - i)):(l - 3 * (z - i) + 3)]
        so_ai = int("".join([str(j) for j in ai]))
        cach_doc.append(doc(so_ai))  # k the dung + print(hang[z]))
        print(hang[z - i - 1])
        cach_doc.append(hang[z - i - 1])
    i= z-1
    ai = a[(l - 3 * (z - i)):(l - 3 * (z - i) + 3)]
    so_ai = int("".join([str(j) for j in ai]))
    if so_ai <= 9:
        print("le")
        cach_doc.append("le")
        print(mot_chuso[so_ai])
        cach_doc.append(mot_chuso[so_ai])
    else :
        cach_doc.append(ba_chuso(so_ai))
#    print(type(cach_doc))   k the in ra dc cai list nay, mặc dù báo là list
    #print(cach_doc)
    return cach_doc
res = doc_so(s)
print(res)
rs = ""
for t in res:
    if isinstance(t, list):
        print(t)
        rs = rs + " " + "".join(t)
    else:
        print(t)
        rs = rs + " " + t
print(rs)




