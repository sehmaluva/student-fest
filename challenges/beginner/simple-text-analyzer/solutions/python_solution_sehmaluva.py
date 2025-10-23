def analyze_text():
    text = input("Enter a sentence or paragraph to analyze:\n")

    if not text.strip():
        print("Input is empty. Please enter some text.")
        return

    words = text.split()
    word_count = len(words)
    char_count = len(text)

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    most_frequent_word = ""
    if word_freq:
        most_frequent_word = max(word_freq, key=word_freq.get)

    unique_words = list(set(words))

    print("\n--- Text Analysis Results ---")
    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")
    if most_frequent_word:
        print(
            f'Most Frequent Word: "{most_frequent_word}" (appears {word_freq[most_frequent_word]} times)'
        )
    print(f"Unique Words: {unique_words}")
    print("\nThank you for using the Simple Text Analyzer!")


if __name__ == "__main__":
    analyze_text()
