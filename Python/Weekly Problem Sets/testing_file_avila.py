## Problem 3 — Song Lyric Word Counter 🎵

# *Pick your favourite song and paste a few verses as a string in your code. Your program will analyse the lyrics using a custom class.*

# **Your task:**

# - **Create a `LyricAnalyzer` class** with the following:
#   - An `__init__` method that accepts a lyrics string
#   - Store the lyrics as an instance attribute
#   - In `__init__`, process the lyrics: use `.lower()` to normalise, `.replace()` to strip punctuation, and `.split()` to create a list of words
#   - Store the processed word list as `self.words`
#   - Add a `count_words()` method that builds and returns a dictionary mapping each word to its count
#   - Add a `unique_word_count()` method that returns the number of unique words (hint: use a set)
#   - Add a `most_common_word()` method that returns a tuple of `(word, count)` for the most frequently used word
#   - Add a `print_report()` method that prints all words alphabetically with their counts, the unique word count, and the most common word

# - In your `__main__` block:
#   - Create a multi-line string variable called `lyrics` with your chosen song lyrics. Here is an example:
  
# ```python
# lyrics = """
# we will we will rock you
# we will we will rock you
# buddy youre a boy make a big noise
# playing in the street gonna be a big man someday
# you got mud on your face you big disgrace
# kicking your can all over the place singing
# we will we will rock you
# """
# ```

#   - Create a `LyricAnalyzer` object with your lyrics
#   - Call the `.print_report()` method

# **Expected output (partial, using example lyrics):**

# ```
# === WORD COUNT ===
# a          : 4
# all        : 1
# be         : 1
# big        : 3
# ...
# we         : 6
# will       : 6
# ...

# Unique words: 26
# Most common word: 'we' — 6 times
# ```

class LyricAnalyzer:
    def __init__(self, lyrics):
        self.lyrics = lyrics

        processed = lyrics.lower()
        processed = processed.replace(".", "")
        processed = processed.replace(",", "")
        processed = processed.replace("!", "")
        processed = processed.replace(":", "")
        processed = processed.replace("'", "")
        processed = processed.replace('"', "")
        processed = processed.replace("?", "")

        self.words = processed.split()


    def count_words(self):
        counts = {}

        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts


    def unique_word_count(self):
        return len(set(self.words))


    def most_common_word(self):
        counts = self.count_words()

        word = max(counts, key=counts.get)

        return (word, counts[word])


    def print_report(self):
        counts = self.count_words()

        print("=== WORD COUNT ===")

        for word in sorted(counts):
            print(f"{word} : {counts[word]}")

        print(f"Unique words: {self.unique_word_count()}")

        word, count = self.most_common_word()

        print(f"Most common word: {word} -- {count} times")

    
if __name__ == "__main__":

    lyrics = """
    Hello world hello Python world
    Hello Python
    """

    analyzer = LyricAnalyzer(lyrics)

    analyzer.print_report()
        
