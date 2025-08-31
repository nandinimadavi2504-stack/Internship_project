def word_counter(filename):
    try:
        # Open the file in read mode
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Split content into words
        words = content.split()
        word_count = len(words)

        print(f"Total words in '{filename}': {word_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# By default, check sample.txt
filename = "Sample.txt"
word_counter(filename)
