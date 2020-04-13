a=int(input("Ingrese primer numero "))
b=int(input("Ingrese segundo numero "))
opt=input ( " Ingrese la operacion :\ n1 ) Suma \ n2 ) Resta \ n3 ) Mult \ n4 ) Div \ n " )
if opt == "1":
    s = a + b
    print("La suma es: " + str(s))
elif opt == "2":
    r = a - b
    print("La resta es: " + str(r))
elif opt == "3":
    m = a * b
    print("La multiplicación es: " + str(m))
elif opt == "4":
    d = a / b
    print("La división es: " + str(d))
else: 
    print("No fue posible realizar operación")
    print(str(a)+" ? "+str(b))
    print("Adios!")
