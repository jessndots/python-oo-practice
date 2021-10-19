"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """finds random words from provided dictionary
    
    >>> wf = WordFinder('simple.txt')
    3 words read

    >>> wf.random() in ["cat", "#hat", "sat"]
    True

    >>> wf.random() in ["cat", "#hat", "sat"]
    True

    >>> wf.random() in ["cat", "#hat", "sat"]
    True
    
    """
    def __init__(self, path):
        """opens file, reads words, prints number of words"""
        self.readWords(path)
        file = open(path)
        self.words = self.readWords(file)
        file.close()
        self.count = len(self.words)
        print(f"{self.count} words read")

    def readWords(self, file): 
        """strips each word in the file and returns list of all words"""
        return [w.strip() for w in file]
        
        

    def random(self):
        """returns random word from words list"""
        return self.words[randint(0, self.count - 1)]


class SpecialWordFinder(WordFinder): 
    """Finds random word from dictionary, excludes comment lines that start with a #
    
    >>> swf = SpecialWordFinder('simple.txt')
    2 words read

    >>> swf.random() in ["cat", "#hat", "sat"]
    True

    >>> swf.random() in ["cat", "#hat", "sat"]
    True

    >>> swf.random() in ["cat", "#hat", "sat"]
    True
    
    """
    def readWords(self, file): 
        """returns list of words in file that do not start with #"""
        return [word.strip() for word in file if not word.strip().startswith("#")]
                