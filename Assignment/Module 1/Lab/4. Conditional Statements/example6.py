num = int(input("Enter a number: "))
flag = 0

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")

