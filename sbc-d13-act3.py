input_word = input("Enter a word: ")

def process_words(word):
    word_list = [w.strip() for w in word]  
    for w in word:
        word_list.append(w)
    print(word_list)

process_words(input_word)