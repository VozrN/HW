def single_root_words(root_word, *other_words):
    other_words_str = []
    for i in other_words:
        other_words_str.append(i)
    for i in range(len(other_words_str)):
        other_words_str[i] = other_words_str[i].lower()
    root_word_str_0=str(root_word)
    root_word_str=root_word_str_0.lower()
    same_words = []
    for word in other_words_str:
        if root_word_str in word or word in root_word_str:
            same_words.append(word)
    return (same_words)


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
