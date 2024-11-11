def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    chars_dict = charactercount(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in chars_dict:
        name = (char["name"])
        num = (char["num"])
        print(f"The {name} character was found {num} times")
    print("--- End report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def wordcount(text):
    words = text.split()
    return len(words)

def charactercount(text):
    charactercount_dict_list = []
    charactercount_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in charactercount_dict:
            charactercount_dict[lowered] += 1
        else:
            charactercount_dict[lowered] = 1
    for character in charactercount_dict:
        character_dict = {}
        if str.isalpha(character) == True:
            character_dict["name"] = character
            character_dict["num"] = charactercount_dict[character]
            charactercount_dict_list.append(character_dict)
    def sort_on(dict):
        return dict["num"]
    charactercount_dict_list.sort(reverse=True, key=sort_on)
    return charactercount_dict_list

main()
