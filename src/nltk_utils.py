import nltk
from nltk.stem.porter import PorterStemmer
#nltk.download('punkt')
stemmer = PorterStemmer()
def tokenize(sentece):
    return nltk.word_tokenize(sentece)

def stem(word):
    return stemmer.stem(word.lower())
    
def bag_of_words(tokenized_sentece, all_words):
    pass
