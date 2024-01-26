print("vítejte v programu na vypočítání S a O obdélníku, V kvádru a S kruhu")


print("zadej 1 pro O obdélníku")
print("zadej 2 pro S obdélníku")
print("zadej 3 pro V kvádru")
print("zadej 4 pro S Kruhu")
print("zadej 5 pro ukončení programu")
vyber = input("co chcete počítat")

if vyber == "1":
    a = input("Zadejte proměnou a:")
    b = input("Zadejte proměnou b:")

    a = int(a)
    b = int(b)

    if a>0 and b>0:
        vysledek = 2*(a+b)
        print(vysledek)


    else:
        print("co to děláš")

elif vyber == "2":
    a = input("Zadejte proměnou a:")
    b = input("Zadejte proměnou b:")

    a = int(a)
    b = int(b)

    if a>0 and b>0:
        vysledek = a*b
        print(vysledek)


    else:
        print("co to děláš")
elif vyber == "3":
    a = input("zadejte propměnou a")
    b = input("zadejte propměnou b")
    c = input("zadejte propměnou c")

    a = int(a)
    b = int(b)
    c = int(c)


    if a>0 and b>0 and c>0:
        vysledek = a*b*c
        print(vysledek)

    else:
        print("co to děláš")

elif vyber == "4":
    r = input("zadejte propměnou r")
    r = int(r)

    if r>0:
        vysledek = 22/7*r
        print(vysledek)
    else:
        print("co to děláš")
elif vyber == "5":
    