"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with (open("referat.txt", "r", encoding="utf-8") as filename):
        text = filename.read()
        print(len(text))
        print(len(text.split()))
        modified_text = text.replace(".", "!")
    with (open("referat2.txt", 'w', encoding="utf-8")) as newfile:
        text_length = newfile.write(str(f'{len(text)} \n'))
        count_words = newfile.write(str(f'{len(text.split())} \n'))
        newfile.write(modified_text)


if __name__ == "__main__":
    main()
