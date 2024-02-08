def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_path):
    txt = get_book_contents(file_path)
    words = txt.split()
    return len(words)

def count_letters(file_path):
    txt = get_book_contents(file_path)
    letters = {}
    for char in list(txt):
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
        
    return letters


def print_report(book_path):
    wc = count_words(book_path)
    lc = count_letters(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the document ")
    dict_list = []
    for k, v in lc.items():
        dict_list.append({'char':k, 'count':v})

    sorted_list = sorted(dict_list, reverse=True, key=lambda x: x['count'])

    for s in sorted_list:
        if s['char'].isalpha():
            print(f"The {s['char']} character was found {s['count']} times")

    print("--- End report ---")

if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    print_report(book_path)
