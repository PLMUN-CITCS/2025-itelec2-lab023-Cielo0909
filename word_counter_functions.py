def count_words_in_sentence(sentence: str) -> int:
    """Returns the number of words in the given sentence."""
    words = sentence.split()
    return len(words)

def main():
    """Main program flow to input a sentence and display the word count."""
    sentence = input("Enter a sentence: ")
    word_count = count_words_in_sentence(sentence)
    print(f"The sentence has {word_count} words.")

if __name__ == "__main__":
    main()
