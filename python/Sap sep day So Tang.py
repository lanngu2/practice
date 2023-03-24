A = [1, 7,2, 5, 9, 3, 12, 19]
B = []


while A:
        min = A[0]
        for x in A:
                if x < min:
                        min = x
        B.append(min)
        A.remove(min)
print(B)