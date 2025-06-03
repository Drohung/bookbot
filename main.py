import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents

from stats import count_words

from stats import character_count

from stats import dictionary_list


def main(input):
    output = get_book_text(input)
    total = count_words(output)
    c_count = character_count(output)
    dictionary_read = dictionary_list(c_count)
    print(f"{total} words found in the document")
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {total} total words
--------- Character Count -------""")
    for i in dictionary_read:
        if i["name"].isalpha() == True:
            print(f"{i["name"]}: {i["num"]}")
    print("============= END ===============")



main(sys.argv[1])

