
num_to_text = {0: '', 1: 'mot', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam', \
            6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin'}
large = {
    1: "muoi",
    2: "tram",
    3: "nghin",
    6: "trieu",
    9: "ty",
}
def read_num(num):
    res = []
    j= 0
    c = num % 10
    m = int(num / 10)
    print(j, m , c)
    text = num_to_text[c]
    if c ==5 and m > 0:
        text = "lam"
    res.append(text)
    while m!=0:
        j = j + 1
        c = m % 10
        m = int(m / 10)
        print(j, m, c)
        i = j
        if i > 9:
            i = i%9
        suf = ""
        if i in large:
            suf = large[i]
        else:
            tmp_i = None
            if i < 6:
                tmp_i = i % 3
            elif i < 9:
                tmp_i = i % 6

            if tmp_i and tmp_i in large:
                suf = large[tmp_i]
            
        text = num_to_text[c] + " " + suf

        # special case
        if c == 1 and suf == "muoi":
            text = "muoi"
        elif c == 0 and suf == "muoi":
            text = "le" 
        elif c == 0:
            text = "khong " + suf
        
        res.append(text)
    res.reverse()
    return res

s = input("number: ")
check = s.isnumeric()
while check == False or int(s) < 0:
    s = input("Please,use positive numbers : ")
    check = s.isnumeric()
    if check == True:
        break
s = int(s)

res = read_num(s)
print(" ".join(res))