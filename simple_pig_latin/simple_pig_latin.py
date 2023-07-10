def pig_latin(sentence):
    piggied_sentence = []
    # split sentence
    split_sentence_list = sentence.split()
    # print(split_sentence_list)

    for word in split_sentence_list:
        # check if the work is from the alphabet
        if word.isalpha():
            # if true then concatinate the first letter to the other letters then add "ay"
            piggied_word = word[1:] + word[0] + "ay"
            # print(piggied_word)
        # if is non-alphabet word dont modify but still rename for appending
        else:
            piggied_word = word

        # add the word to the sentence list
        piggied_sentence.append(piggied_word)
    
    # format the list into a sentence with join()
    final_piggied_sentence = " ".join(piggied_sentence)
    
    return final_piggied_sentence


print(pig_latin("beep boop !"))
