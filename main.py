import string

def main():
    book_path = './books/frankenstein.txt'
    book_text = get_book_content(book_path)
    num_words = counter_words(book_text)
    num_letters = count_letters(book_text)
    sortedLetter = sort_on(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print_report(sortedLetter)
    print(f"--- End Report ---")


def get_book_content(path):
    with open(path) as f:
        return f.read()

def counter_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    alphabet = string.ascii_lowercase
    letters = {}
    for letter in alphabet:
        letters[letter] = text.count(letter)

    return letters

def sort_on(letters):
    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_letters)


def print_report(letterSorted): 
    for key,value in letterSorted.items():
        print(f"the {key} character was found '{value}' times")


main()



