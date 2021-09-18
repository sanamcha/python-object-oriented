import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """Find random words form words.txt
    >>> w = WordFinder("words.txt") 
    235886 words read   
    """

    def __init__(self, path):
        """Reads words from file words.txt """
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        return [w.strip() for w in file]

    def random(self):
        """show random words"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """WordFinder that will not includes comments and blank lines.
    >>> s = SpecialWordFinder("words2.txt")
    10 words read
    >>> s.random() in ["tomatoes","kale","parsnips","brocolli","cucumber","apple","mango","banana","cherry","pineapple"]
    True
    >>> s.random() in ["# Veggies","# Fruits"]
    False
    """
    def parse(self, file):
        """It will parse the file skipping the comments and blank lines.
        """      
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]
    



