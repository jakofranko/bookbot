def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        char_count = num_characters(file_contents)
        print(len(words))
        print('')
        char_report(file_contents)


def num_characters(s):
    char_count = {}
    for letter in s:
        l = letter.lower()
        if (l in char_count) == False:
            char_count[l] = 0

        char_count[l] += 1

    return char_count

def sort_char_count(char_count):
    char_items = char_count.items()
    sorted_chars = sorted(char_items, key=lambda item: item[1], reverse=True)
    return {k: v for k, v in sorted_chars}

def char_report(text):
    char_count = num_characters(text)
    sorted_chars = sort_char_count(char_count)

    for char in sorted_chars:
        print(f"The '{char}' character was found {sorted_chars[char]} times")

        

main()
