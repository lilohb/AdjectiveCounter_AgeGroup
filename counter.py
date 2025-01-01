import re
import os

def read_words_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        exit()

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        cleaned_content = re.sub(r'[^\w\s]', '', content)
        words = cleaned_content.split() 
    return words


def count_words_frequencies(words_list):
    words_frequencies = {}

    for word in words_list:
        item = word.lower()
        words_frequencies[item] = words_frequencies.get(item, 0) + 1

    return words_frequencies


if __name__ == "__main__":
    #Ask the user to enter the file name
    file_name = input("Enter the name of the text file (with extension): ")



    words_list = read_words_from_file(file_name)
    words_frequencies = count_words_frequencies(words_list)

    sorted_dict = dict(sorted(words_frequencies.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)


