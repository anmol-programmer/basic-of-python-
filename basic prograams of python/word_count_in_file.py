# Function to count words in a file
def count_words():
    # Open the file named 'sample.txt' in read mode
    with open("notes.txt", "r") as file:
        content = file.read()             # Read the entire file content
        words = content.split()           # Split content into words based on whitespace
        word_count = len(words)           # Count the number of words
        print("Total number of words:", word_count)

# Main program starts here
print("Word Count Program")
print("====================")
count_words()                             # Call the function
