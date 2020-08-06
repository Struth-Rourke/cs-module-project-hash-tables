# Your code here
def histogram(filename):
    # get file's contents with open
    with open(filename) as f:
        s = f.read()
    
    # list of symbols that are 
    symbols_list = ['"',':',';',',','.','-','+','=','/','|','?',
                    '\\','[',']','{','}','(',')','*','&','^','!']
    
    # loop through the symobls in the symbols_list
    for symbol in symbols_list:
        # replace the symbol with nothing and save over the original variable
        s = s.replace(symbol, "")
    # lower case all the remaining words for uniformity
    s = s.lower()
    # splitting all the words out individually and saving to a variable
    word_list = s.split()

    # instantiate total_word_count tracker
    total_word_count = 0
    # isntantiate max_word_length tracker
    max_word_length = 0
    # isntantiate word_counts dict to hold all the words and their respective 
    # counts
    word_counts = {}
    # loop over the words in the word_list
    for word in word_list:
        # if the length of the word is greater thab the current max
        if len(word) > max_word_length:
            # set the lengt variable to the len of the word
            max_word_length = len(word)
        # if the word is not already in the dictionary
        if word not in word_counts:
            # set the value of that word in the dictionary equal to one
            word_counts[word] = 1
        # if the word is already in the dictionary
        else:
            # add to the already exisitng value in the dictionary for the
            # specified word
            word_counts[word] += 1
        # add to the total_word_count tracker variable
        total_word_count += 1
    # add to max_word_length
    max_word_length += 2
    
    # sort by word counts
    word_counts = sorted(word_counts.items(), reverse=True, key=lambda item: item[1])

    # loop over the words in the word_counts
    for word in word_counts:
        # instantiate empty string varaible
        hashtag_hist = ""
        # add the word at the first index to the string
        hashtag_hist += word[0]
        # add, via join, a space for x in range of the max_word_length - len 
        # of the word at the first index
        hashtag_hist += "".join([" " for x in range(max_word_length - len(word[0]))])
        # add, via join, a '#' for the amount of times each word comes up in the
        # value column of the dict
        hashtag_hist += "".join(["#" for x in range(word[1])])
        # print the results
        print(hashtag_hist)

if __name__ == "__main__":
    histogram("robin.txt")
