def print_full_name(a, b):
    if len(a + b) > 10:
        print("Name too big. Try again")
    else:
        print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)