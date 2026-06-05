import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')  # WordNet data download karna zaroori hai lemmatization ke liye
# Tools initialize karein
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

word = "changing"
print("Original Word:", word)
# Stemming test
print("Stemming Result:", stemmer.stem(word)) 
# Output: chang (Aakhir se 'ing' kaat diya, 'e' gayab ho gaya)

# Lemmatization test (Humne bataya ke yeh ek Verb hai)
print("Lemmatization Result:", lemmatizer.lemmatize(word, pos='v')) 
# Output: change (Sahi meaningful base word mila!)
another_word = "better"
print("\nOriginal Word:", another_word)