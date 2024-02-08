class BookBot:
    """
    A python bot that analyzes text and extracts information.

    Attributes:
        word_count - total count of words in a text
        char_count - a list of alphanumeric characters and their counts, sorted 
                     by char count in descending order

    """
    def __init__(self, txt):
        self.txt = txt
        self.word_count = self.count_words()
        self.char_count = self.count_chars()
        self.report = None

    def get_book_contents(self):
        """Read text contents of a file"""
        with open(self.txt) as f:
            file_contents = f.read()
        return file_contents

    def count_words(self):
        """Count words in a given text"""
        txt_contents = self.get_book_contents()
        words = txt_contents.split()
        return len(words)
    
    def __chars_to_dict(self):
        txt_contents = self.get_book_contents()
        letters = {}
        for char in list(txt_contents):
            char = char.lower()
            if char.isalpha():
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
        return letters
    
    def __dict_to_list(self, dict):
        dict_list = []
        for k, v in dict.items():
            dict_list.append({'char': k, 'count': v})
        return dict_list
    
    def __sort_dict_list(self, lst):
        return sorted(lst, reverse=True, key=lambda x: x['count'])


    def count_chars(self):
        """
        Count alphanumeric characters in a given text. Return a list of dicts 
        sorted descending by count.
        """
        char_dict = self.__chars_to_dict()
        char_list = self.__dict_to_list(char_dict)
        return self.__sort_dict_list(char_list)


    def print_report(self):
        """`Generate a report detailing word count and character count"""
        print(f"--- Begin report of {book_path} ---")
        print(f"{self.word_count} words found in the document ")
        for c in self.char_count:
            print(f"The {c['char']} character was found {c['count']} times")
        print("--- End Report ---")



if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    b = BookBot(book_path)
    b.print_report()
