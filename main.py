def main():
    #sets the location of the book
    book_location = "books/frankenstein.txt"
    #gets the text from the file in book_location
    text = open_file(book_location)
    #prints the number of words in text
    print(get_num_words(text))
    #get the count of all characters
    chars_count = count_chars(text)
    print(chars_count)

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


main()
