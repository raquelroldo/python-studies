

def transformer():
    name = input("Digite seu nome ")
    name = name.upper()
    transf = ""
    for x in reversed(name):
        transf = transf + x
    print(transf)

transformer()