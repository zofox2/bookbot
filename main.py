def main():
   
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_chars(text)
    list_from_dict = list(num_characters.items())
    list_from_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in list_from_dict:
        print(f"The {char[0]} character was found {char[1]} times")
    print("---- End report ---")

def get_num_chars(text):
    character_dict = {}
    lowered = text.lower()
    s_lowered = list(lowered)
    for i in s_lowered:
        if i.isalpha():
            if i in character_dict:
                character_dict[i] += 1 
            else:
                character_dict[i] = 1
    
    return character_dict
   
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict[1]
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()