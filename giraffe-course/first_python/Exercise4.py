

def transformer():
    name = input("Enter your name ")
    name = name.upper()
    transf = ""
    for x in reversed(name):
        transf = transf + x
    print(transf)

transformer()