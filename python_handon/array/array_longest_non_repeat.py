    #Given a string, find the length of the longest substring,
    # without repeating characters.

    # Examples:
   
    # Given \"abcabcbb\", the answer is \"abc\", which the length is 3.\n",
    # Given \"bbbbb\", the answer is \"b\", with the length of 1.\n",
    # Given \"pwwkew\", the answer is \"wke\", with the length of 3.\n",

phrase = "abcedfabcbb"
def longest_substring(phrase):
    max_len = 0

    for i,c in enumerate(phrase): # c representa o caracter na posicao i
        start = i
        substring = []
    
        while (start < len(phrase)) and (phrase[start] not in substring):
            substring.append(phrase[start])  
            start += 1
        print(substring) 

        if max_len < len(substring):
            max_len = len(substring)   
    print(max_len)

    return max_len

longest_substring(phrase)    
