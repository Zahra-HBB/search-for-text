from search import search


def main():
    text_file = open("./data/usa/usa.txt", "r")
    english_words = text_file.readlines()

    search_term = input("Please enter a string: ")

    string_count = search(english_words, search_term)

    if string_count["str_count"] == 0:
        print("No occurance found!")
    else:
        print("Total number of '{}' occurance is: {} \nThe longest word includes input is: {}".format(
            search_term, string_count["str_count"], string_count["max_text"]))


if __name__ == '__main__':
    main()
