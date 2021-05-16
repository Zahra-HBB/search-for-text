string_count = {
    "str_count": 0,
    "max_text": ''
}


def search(english_words, search_term):

    for line in english_words:
        if search_term in line:
            string_count["str_count"] = string_count["str_count"] + 1

            if len(string_count["max_text"]) <= len(line):
                string_count["max_text"] = line
    return string_count
