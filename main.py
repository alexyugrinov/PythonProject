s = str(input("Введите выражение типа a b c , где a и c - целые числа, а b - операция +, -, *, / "))

d=s.split()

if len(d) == 3:
    a, b, c = s.split()
    a = int(a)
    c = int(c)

    if (a in range(1, 11)) & isinstance(a, int) & (b == "+") & (c in range(1, 11)) & isinstance(c, int):
        print(a + c)
    elif  (a in range(1, 11)) & isinstance(a, int) & (b == "-") & (c in range(1, 11)) & isinstance(c, int):
        print(a - c)
    elif  (a in range(1, 11)) & isinstance(a, int) & (b == "*") & (c in range(1, 11)) & isinstance(c, int):
        print(a * c)
    elif (a in range(1, 11)) & isinstance(a, int) & (b == "/") & (c in range(1, 11)) & isinstance(c, int):
        print(a // c)
    else:
        print("throws Exception")


