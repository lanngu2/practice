mot_chuso = {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
mot_bon_lam = {0: '', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'lam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
hangdonvi_db = {0: '', 1: 'mốt', 2: 'hai', 3: 'ba', 4: 'tư', 5: 'lam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
hang_chuc = {0: '', 1: 'muoi', 2: 'hai muoi', 3: 'ba muoi', 4: 'bon muoi', 5: 'nam muoi', \
            6: 'sau muoi', 7: 'bay muoi', 8: 'tam muoi', 9: 'chin muoi'}
hang_tram = {0: '', 1: 'mot tram', 2: 'hai tram', 3: 'ba tram', 4: 'bon tram', 5: 'nam tram', \
            6: 'sau tram', 7: 'bay tram', 8: 'tam tram', 9: 'chin tram'}
so_duoi = {1: 'linh một', 2: 'linh hai', 3: 'linh ba', 4: ' linh bon', 5: 'linh nam', \
            6: 'linh sau', 7: 'linh bay', 8: 'linh tam', 9: 'linh chin'}
hang = {0: '', 1: 'nghin', 2: 'trieu', 3: 'ti', 4: 'nghin ti', 5: 'trieu ti', \
            6: 'ti ti', 7: 'nghin ti ti', 8: 'trieu ti ti', 9: 'ti ti ti'}
def so_1_chuso(so1chuso):
    doc1chuso = []
    if so1chuso >= 0 and so1chuso < 10:
        doc1chuso = mot_chuso[so1chuso]
    return doc1chuso
def hang_donvi(donvi):
    docdonvi = []
    docdonvi = hangdonvi_db[donvi]
    return docdonvi
def so_2_chuso(so2chu): # lon hon 9, neu 02 la error
    doc2chuso = []
    if so2chu//10 == 1 and so2chu%10 != 0:
        doc2chuso = hang_chuc[1] + " " + mot_bon_lam[so2chu%10]
    elif so2chu//10 == 1 and so2chu%10 == 0:
        doc2chuso = hang_chuc[1]
    elif so2chu%10 ==0:
        doc2chuso = hang_chuc[so2chu//10]
    else:
        doc2chuso = hang_chuc[so2chu//10] + " " + hangdonvi_db[so2chu%10]
    return doc2chuso
def so_3_chuso(so3chuso):# lon hon 100
    doc3chuso = []
    if (so3chuso%100)//10 == 0 and (so3chuso%100)%10 != 0:
        doc3chuso = hang_tram[so3chuso//100] + " " + so_duoi[(so3chuso%100)%10]
    elif (so3chuso%100)//10 == 0 and (so3chuso%100)%10 == 0:
        doc3chuso = hang_tram[so3chuso//100]
    else:
        doc3chuso = hang_tram[so3chuso//100] + " " + so_2_chuso(so3chuso%100)
    return doc3chuso
def cum_3so(cum3so):
    doc_cum3so = []
    if cum3so >= 0 and cum3so < 10:
        doc_cum3so = so_1_chuso(cum3so)
    if cum3so > 9 and cum3so < 100:
        doc_cum3so = so_2_chuso(cum3so)
    if cum3so > 99 and cum3so < 1000:
        doc_cum3so = so_3_chuso(cum3so)
    return doc_cum3so
def so_lon(a):
    cach_doc = []
    a = list(str(a))
    l = len(a)
    z = l // 3
    d = l % 3
    k = z-1
    aik = a[(l - 3 * (z - k)):(l - 3 * (z - k) + 3)]
    so_aik = int("".join([str(j) for j in aik]))
    if d == 0:
        cach_doc = ""
        for i in range(0, (z - 1)):
            ai = a[(l - 3 * (z - i)):(l - 3 * (z - i) + 3)]
            so_ai = int("".join([str(j) for j in ai]))
            cach_doc = cach_doc + " " + cum_3so(so_ai) + " " + hang[z - i - 1] + ","
        if so_aik <= 9:
            cach_doc = cach_doc + " " + so_duoi[so_aik]
        else:
            cach_doc = cach_doc + " " + cum_3so(so_aik)
    if d == 1:
        a0 = int(a[0])
        cach_doc = so_1_chuso(a0) + " " + hang[z]
        for i in range(0, (z - 1)):
            ai = a[(l - 3 * (z - i)):(l - 3 * (z - i) + 3)]
            so_ai = int("".join([str(j) for j in ai]))
            cach_doc = cach_doc + " " + cum_3so(so_ai) + " " + hang[z - i - 1]
        if so_aik <= 9:
            cach_doc = cach_doc + " " + so_duoi[so_aik]
        else:
            cach_doc = cach_doc + " " + cum_3so(so_aik)
    if d == 2:
        a12 = a[0:2]
        doi_a12 = [str(i) for i in a12]
        so_a12 = "".join(doi_a12)
        so_a12 = int(so_a12)
        cach_doc = so_2_chuso(so_a12) + " " + hang[z]
        for i in range(0, (z - 1)):
            ai = a[(l - 3 * (z - i)):(l - 3 * (z - i) + 3)]
            so_ai = int("".join([str(j) for j in ai]))
            cach_doc = cach_doc + " " + cum_3so(so_ai) + " " + hang[z - i - 1]
        if so_aik <= 9:
            cach_doc = cach_doc + " " + so_duoi[so_aik]
        else:
            cach_doc = cach_doc + " " + cum_3so(so_aik)
    return cach_doc

s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)

def docsochuan(socandoc):
    doc_sochuan = []
    if socandoc >=0 and socandoc < 1000:
        doc_sochuan = cum_3so(socandoc)
    else:
        doc_sochuan = so_lon(socandoc)
    return doc_sochuan

res = docsochuan(s)
print(res)
