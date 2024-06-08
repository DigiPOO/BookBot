def main():
    #sets the location of the book
    book_location = "books/frankenstein.txt"
    #gets the text from the file in book_location
    text = open_file(book_location)
    #get the count of all characters
    chars_count = count_chars(text)
    fancy_print(book_location, text, chars_count)
    

def open_file (location):
    #open the file
    with open(location) as file:
        #read the file
        data = file.read()
    #returns the read data    
    return data

def get_num_words(text):
    #splits the text into words
    words = text.split()
    #returns the number of wrods in the text
    return len(words)

def count_chars(text):
    #creates a dictionary for storing the different occuring characters and their count
    chars_count = {}
    #for each of the characters in the text
    for char in text:
        #converts the character to lowercase if applicable
        lowered = char.lower()
        #if the character is aready in the dictionary, increase its count by 1
        if lowered in chars_count:
            chars_count[lowered] = chars_count[lowered] + 1
        #else the character is not in the dictionary and sets it count to 1
        else:
            chars_count[lowered] = 1
    #returns the dictionary
    return chars_count

def fancy_print(book_location, text, chars_count):
    print(f"--- Begin report of {book_location} ---")
    print(f"{get_num_words(text)} words found in the document")
    #sets up a list of all the letters in the alphabet; all lowercase
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #for each of the letters it will print the number of times it occurs 
    for letter in letters:
        print(f"The '{letter}' character was found {chars_count[letter]} times")
    print("--- End report ---")

main()
