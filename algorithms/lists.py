# actions = {
#     '1 insert': insert(),
#     '2 print': print(),
#     '3 remove': remove(),
#     '4 append': append(),
#     '5 sort': sort(),
#     '6 pop': pop(),
#     '7 reverse': reverse()
# } 
# print(actions)

if __name__ == '__main__':
    N = int(input())

    lis = []
    lis.insert(0,5)
    lis.insert(1,10)
    lis.insert(0,6)
    print(lis)
    lis.remove(6)
    lis.append(9)
    lis.append(1)
    lis.sort()
    print(lis)
    lis.pop()
    lis.reverse()
    print(lis)
