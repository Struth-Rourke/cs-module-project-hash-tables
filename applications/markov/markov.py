import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

## TODO: analyze which words can follow other words

# instantiate empty dictionary
mdict = {}
# split the words in the input.txt file
word_list = words.split()
# instantiate empty list to store capitalized words since they start sentences
start_words = []
# instantiate prev_word as None so it can be filled later
prev_word = None

# for a word in the word_list
for word in word_list:
    # Check for the first word
    if prev_word == None:
        # set the first word as the now pre_word in the chain
        prev_word = word
        # continue iterating
        continue
    # identify words that end in concluding punctuation marks
    if prev_word.endswith(('.', '?', '!', '"')):
        # instantiate list for value in mdict
        mdict[prev_word] = []
        # set the previous word equal to the word to move forward
        prev_word = word
        # continue
        continue
    # if the word in not in the dictionary
    if prev_word not in mdict:
        # if the first letter (at index 0) of that word is capitalized
        if prev_word[0].isupper():
            # addd it to the start_words list
            start_words.append(prev_word)
        # else, set the word (in a list) equal to the value
        mdict[prev_word] = [word]
    # else the word is in the dictionary
    else:
        # append the word (value)
        mdict[prev_word].append(word)
    # move to the next word
    prev_word = word


## TODO: construct 5 random sentences

# loop through 5 times
for _ in range(5):
    # sentence variable is equal to a random choice of start_words
    sentence = [random.choice(start_words)]
    # loop through 
    for i in range(100):
        # append a randomly chosen word value from the dictionary to the sentence
        # with the already chosen start_word
        sentence.append(random.choice(mdict[sentence[i]]))
        # if the word at the index ahead of it ends with a punctuation mark that
        # concludes a sentence
        if sentence[i + 1].endswith(('.', '?', '!', '"')):
            # break the loop as the sentence is finished
            break
    # print the join of a space and the words in the sentence variable
    print(" ".join(sentence))
