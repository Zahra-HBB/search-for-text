text_file = open("./data/usa/usa.txt", "rt")
english_words = text_file.readlines()

string_count = {
    "str_count": 0,
    "max_text": ''
}

input = input("Please enter a string: ")


def search():
    if input in line:
        string_count["str_count"] = string_count["str_count"] + 1

        # if there are more than one accurance with the same lenghth bigger than the input value, the last occurance will return
        if len(string_count["max_text"]) <= len(line):
            string_count["max_text"] = line


for line in english_words:
    search()

print("Total number of '{}' occurance is: {} \nThe longest word includes input is: {}".format(
    input, string_count["str_count"], string_count["max_text"]))