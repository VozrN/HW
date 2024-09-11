def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word:
            same_words.append(word)
    print(f'Слова, содержащие "{root_word}" в составе слова: {same_words}')


other_words_full = input('Введите в строку любые слова: ')
other_words = other_words_full.lower()
other_words_split = other_words.split()
root_word_full = input('Слова с каким корнем/частью слова будем искать: ')
root_word = root_word_full.lower()
single_root_words(root_word, *other_words_split)
