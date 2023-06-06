# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


with open(r'C:\Users\ka.chernyh\PycharmProjects\pythonProject2\9\test_file\task1_data.txt', 'r', encoding='utf-8') as f1:
    text = f1.read()
    text1 = ''
    for c in text:
        if c.isalpha():
          text1 = text1 + c
#    new_text = ''.join(c for c in text if c.isalpha())
with open(r'C:\Users\ka.chernyh\PycharmProjects\pythonProject2\9\test_file\task1_answer.txt', 'w', encoding='utf-8') as f2:
      f2.write(text1)




#     open(r'C:\Users\ka.chernyh\PycharmProjects\pythonProject2\9\test_file\task1_answer.txt', 'w', encoding='utf-8') as f2:



#    for line in f1.readline():
#         new_line = ''.join(c for c in f1 if c.isalpha())
#         f2.write(new_line)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
