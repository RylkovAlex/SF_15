import os

file_name = input('Введите имя файла:\n')

def get_keys_by_value(dict, condition):
    """
    Функция принимает словарь и условие.
    Возвращает список ключей словаря, для значений которых выполняется условие.
    """
    results = []
    for k, v in dict.items():
        if condition(v):
            results.append(k)
    return results

try:
    file = open(os.path.join(os.getcwd(), file_name), 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
except FileNotFoundError:
    print(f'Фал c именем {file_name} не найден в рабочей дирректроии: {os.getcwd()}')

eng_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequency = {}
max_len_words = []

for i, word in enumerate(file_data.split()):
    if i == 0:
        max_len_words.append(word)
    if len(word) > 3:
        frequency[word] = 1 if not word in frequency else frequency[word] + 1
    if all(char in eng_chars for char in word):
        # Если допускаем смешанный язык в одном слове, то можно: if any(char in word for char in eng_chars):
        if len(word) > len(max_len_words[0]):
            max_len_words = [word]
        elif len(word) == len(max_len_words[0]) and word not in max_len_words:
            max_len_words.append(word)

max_frequencys = get_keys_by_value(frequency, lambda value: value == max(frequency.values()))

print(f'Слово(а) наиболее часто встречающееся в тексте из тех, что имеют размер более трех символов:\n{"".join(max_frequencys)}')
print(f'Наиболее длинное(ые) в тексте слово(а) на английском языке:\n{" ".join(max_len_words)}')
