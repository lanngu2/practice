k = input("How many first numbers of Fibonacci do you want to print and summarize: ")
check = k.isnumeric()
while check == False or int(k) < 0:
    k = input("Please,use positive numbers : ")
    check = k.isnumeric()
    if check == True:
        break

k = int(k)
def fibonacci(n):
    n = int(n)
    f0 = 1
    f1 = 1
    fn = 1
    if n < 0:
        return 0;
    elif n == 0 or n == 1:
        return 1;
    else:
        for i in range(2,n + 1):
            f0 = f1
            f1 = fn
            fn = f0 + f1
    return fn;
sumx = 0
for i in range (0,k):
   # print("i = ", i)
    x = fibonacci(i)
    print("f", i ,"=", x)
    sumx = sumx + fibonacci(i)
    print("Summary of the first", i + 1 , "numbers is:", sumx)
