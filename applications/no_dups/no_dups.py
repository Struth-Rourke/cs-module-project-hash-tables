def no_dups(s):
    # instantiate empty lookup
    word_lookup = {}
    # split the words in the string
    word_list = s.split()
    # for a word in word_list
    for word in word_list:
        # since dictionaries don't allow dups, if a word does not already exist
        if word not in word_lookup:
            # add the word to the lookup with the 
            word_lookup[word] = word

    s_out = " ".join(word_lookup.values())
    return s_out
    
    # return s_out



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))