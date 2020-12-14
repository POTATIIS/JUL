def plus(x, y):
    return x + y

def minus(x, y):
    return x - y    

def gånger(x, y):
    return x * y    

def delat(x, y):
    return x / y

print("Hur ska tomten räkna. ")
print("1.plus")    
print("2.minus")
print("3.gånger")
print("4.delat")
print("5.Tomten hand slant")
while True:
    alternativ = input("Välj Tomtens räknesätt: ")
    if alternativ in ('1', '2', '3', '4'):
        nummer1 = float(input("Välj den första siffran: "))
        nummer2 = float(input("Välj den andra siffran: "))
    if alternativ == '5':
        print("Tomten säger hej då")
        break
    elif alternativ == '1':
        print(nummer1, "+", nummer2, "=", plus(nummer1, nummer2))        
    elif alternativ == '2':
        print(nummer1, "-", nummer2, "=", minus(nummer1, nummer2))        
    elif alternativ == '4':
        print(nummer1, "/", nummer2, "=", delat(nummer1, nummer2))
        break
    

    else:
        print("Var försiktig, tomten har en sawed off")
