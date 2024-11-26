def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    
    def words_in_file(file_contents):
        words = file_contents.split()
        return len(words)
    # print(words_in_file(file_contents))
    
    def times_char_in_file(file_contents):
        file_contents = file_contents.lower()
        char_count = {char: file_contents.count(char) for char in set(file_contents) if char.isalpha()}
        for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
            print(f"The '{char}' character was found {count} times")
        return char_count
    times_char_in_file(file_contents)
main()

