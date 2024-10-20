class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words_split = []
                for each_string in file:
                    each_string = each_string.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for clear_punctuation in punctuation:
                        each_string = each_string.replace(clear_punctuation, '')
                    words_split.extend(each_string.split())

            all_words[file_name] = words_split
        return all_words

    def find(self, word):
        find_list = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_list[name] = words.index(word.lower()) + 1

            return find_list

    def count(self, word):
        count_list = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_list[name] = words.count(word.lower())

            return count_list


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
