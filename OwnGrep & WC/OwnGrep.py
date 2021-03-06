import abc

class NotANumber(Exception):
    pass


class NotAString(Exception):
    pass


class InputStringValidator:
    def __init__(self , string):
        self.filename = string

    def valid(self):
        if not self.is_string(self.filename):
            raise NotAString();

    def is_string(self, string):
        return isinstance(string, str)


class InputValueValidator:
    def __init__(self, value):
        self.files_value = int(value)

    def valid(self):
        if not self.is_number(self.files_value):
            raise NotANumber()

    def is_number(self, value):
        return isinstance(value, int)


class SearchEngine:
    def __init__(self):
        self.files_tab = []
        self.items_found = 0
        self.file_amount = int(input("Podaj liczbe plikow do przeszukania: "))
        value_validator = InputValueValidator(self.file_amount)
        value_validator.valid()

        for i in range(self.file_amount):
            self.files_tab.append(input("Podaj nazwe " + str(i + 1) + " pliku: " ))
            string_validator = InputStringValidator(str(self.files_tab[i]))
            string_validator.valid()

        self.searched_phrase = input("Podaj poszukiwane wyrazenie: ")
        string_validator = InputStringValidator(str(self.searched_phrase))
        string_validator.valid()
        self.results = open("found.txt", "w")

    def search(self, file , phrase):
        file_to_search = open(file , "r")
        self.results.write("Phrase \"" + phrase + "\" found in file \"" + file + "\" in: \n")
        line_count = 0
        for line in file_to_search:
            line_count += 1
            if not line.find(phrase) == -1:
                self.results.write("LINE: " + str(line_count) + "  " + line)
                self.results.write("\r\n")


x = SearchEngine()
print(x.files_tab)
for i in x.files_tab:
    x.search(i , x.searched_phrase)