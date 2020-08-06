def word_count(s):
    # instantiate list of the symbols we want to ignore
    symbols_list = ['"',':',';',',','.','-','+','=','/','|',
                    '\\','[',']','{','}','(',')','*','&','^']
    # loop over the symbols in the symbols_lsit
    for symbol in symbols_list:
        # replace all the symbol with nothing and save over the variable
        s = s.replace(symbol, '')
    # instantiate word_list that is a list of the split words lowered for uniformity
    word_list = s.lower().split()
    # instantiate an empty dictionary
    word_dict = {}
    # for a word in the word_list
    for word in word_list:
        # if the word is not in the word_dict
        if word not in word_dict:
            # set the value for the word in the dict as 1
            word_dict[word] = 1
        # otherwise, if it already exists
        else:
            # add one to the value that already exists
            word_dict[word] += 1
    # return the dictionary
    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
