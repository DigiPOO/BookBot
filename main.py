def main():
    #sets the location of the book
    book_location = "books/frankenstein.txt"
    #gets the text from the file in book_location
    text = open_file(book_location)
    #prints the number of words in text
    print(get_num_words(text))

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

def count_letters(test):
    return

main()
