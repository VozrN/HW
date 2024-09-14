def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        i = word.lower()
        if root_word.lower() in i or i in root_word.lower():
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
