def mutate_string(string, position, character):
    new_word = list(string)
    new_word[position] = character
    word = "".join(new_word)
   
    return word


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
