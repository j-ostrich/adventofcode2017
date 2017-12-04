def no_duplicates(words):
    # initialize set to add words to and check for duplicates
    word_set = set()
    # iterate over list of words
    for word in words:
        # if the word is found in our word set then it's a duplicate so return False
        if word in word_set:
            return False
        # if word wasn't in word_set, add it
        word_set.add(word)
    # if we get through all of the words without a duplicate then we can return True
    return True

# Same as `no_duplicates` except sort the words before checking/adding
# (use a tuple because sorted returns a list and listed aren't hashable)
# for example, "jonathan" and "taanhjno" both become ('a', 'a', 'h', 'j', 'n', 'n', 'o', 't')
# so if "jonathan" has already been added then "taanhjno" will be found in the set
def no_anagrams(words):
    anagram_set = set()
    for word in words:
        sorted_letters = tuple(sorted(word))
        if sorted_letters in anagram_set:
            return False
        anagram_set.add(sorted_letters)
    return True

if __name__ == "__main__":
    # Parse input by making a list of lists
    with open("problem4_input.txt") as f:
        words_list = [line.strip().split(" ") for line in f.readlines()]

    # filter the list by the appropriate function
    print("Valid (no duplicates): %s" % len([words for words in words_list if no_duplicates(words)]))
    print("Valid (no anagrams): %s" % len([words for words in words_list if no_anagrams(words)]))
