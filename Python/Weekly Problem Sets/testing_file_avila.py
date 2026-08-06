class LyricAnalyzer():
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
                counts[word] +=1
            else:
                counts[word] =1

        return counts

    def unique_word_count(self):
        return len(set(self.words))


    def most_common_word(self):
        counts =self.count_words()
        word = max(counts, key=counts.get)
        return (word, counts[word])

    def print_report(self):
        counts = self.count_words()

        
        print(" === Word Count === ")

        for word in sorted(counts):
            print(f"{word} : {counts[word]}")

        print(f"Unique words: {self.unique_word_count()}")

        word, count = self.most_common_word()

        print(f"Most common word: {word} -- {count} times")

if __name__ == "__main__":
    lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""
    
    analyzer = LyricAnalyzer(lyrics)

    analyzer.print_report()
        
