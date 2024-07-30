# 1. Tokenization
# Tokenization is the process of splitting text into individual words or sentences. This step is essential for breaking down the text into manageable pieces.

import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize

text = "Natural Language Processing is fascinating."
tokens = word_tokenize(text)
print(tokens)

# 2. Stemming
# Stemming reduces words to their base or root form. It is useful for text normalization.

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "ran", "runs"]
stems = [stemmer.stem(word) for word in words]
print(stems)

# 3. Lemmatization
# Lemmatization is similar to stemming but more accurate as it reduces words to their base form using a dictionary.

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
words = ["running", "ran", "runs"]
lemmas = [lemmatizer.lemmatize(word, pos='v') for word in words]
print(lemmas)

# 4. Stop Words
# Stop words are common words (like "is", "and", "the") that are often removed from text before processing, as they carry less meaningful information.

from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
# print(stop_words)
filtered_text = [word for word in tokens if word.lower() not in stop_words]
print(filtered_text)

"""
Overview of Popular NLP Libraries

NLTK (Natural Language Toolkit)
NLTK is a powerful library for various NLP tasks, including tokenization, stemming, lemmatization, and more.

SpaCy

SpaCy is an open-source software library for advanced NLP tasks, known for its speed and efficiency.

TextBlob
TextBlob is a simple library for processing textual data, providing easy-to-use APIs for common NLP tasks.


Introduction to Chatbot Frameworks

ChatterBot

ChatterBot is a Python library that makes it easy to generate automated responses to a user's input.

Rasa

Rasa is an open-source framework for building conversational Al, including chatbots and voice assistants.
"""
