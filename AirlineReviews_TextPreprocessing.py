# -*- coding: utf-8 -*-
"""NLP_assignment01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RB3hosxuzML1q2K3zVbzwpFKn_LANBwd

HAFSA HAFEEZ SIDDIQUI (02-136212-026)

TEXT NORMALIZATION & DATA CLEANING
"""

#importing libraries
import pandas as pd
import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

#reading the dataset
from google.colab import drive
drive.mount('/content/drive')

data_dir = '/content/drive/MyDrive/Airline_review.csv'
df = pd.read_csv(data_dir)

df.head()

print(df.shape)

df.info()

"""REMOVAL OF PUNCTUATION MARKS:

Punctuation marks such as commas, periods, exclamation marks, and question marks serve grammatical purposes but
often do not contribute to the semantic meaning of text in NLP tasks. Removing punctuation marks helps in standardizing text and reducing noise.

1.   the string.punctuation constant from the string module is used to define a string containing all punctuation marks. This string includes characters such as "!", ".", ",", "?", etc.
2.   '[{}]'.format(punctuation) constructs a regular expression pattern to match any punctuation mark contained in the punctuation string.
3.    str.replace() then replaces any occurrence of punctuation marks in the specified column with an empty string, effectively removing them from the text.

"""

# Define the punctuation marks to be removed
punctuation = string.punctuation

# Remove punctuation
df["Review_Title"] = df["Review_Title"].str.replace('[{}]'.format(punctuation), '')
df["Review"] = df["Review"].str.replace('[{}]'.format(punctuation), '')
df["Seat Type"] = df["Seat Type"].str.replace('[{}]'.format(punctuation), '')
df["Route"] = df["Route"].str.replace('[{}]'.format(punctuation), '')
df["Airline Name"] = df["Airline Name"].str.replace('[{}]'.format(punctuation), '')
df["Type Of Traveller"] = df["Type Of Traveller"].str.replace('[{}]'.format(punctuation), '')

"""CONVERTING TO LOWERCASE:

By converting all letters to lowercase, the vocabulary size is effectively reduced, as the same word in different cases is treated as a single token.

1.   str.lower() converts all letters in the text to lowercase, leaving any non-alphabetic characters unchanged.
2.   Each column's text data is transformed, ensuring that variations in letter case are normalized across all columns.

"""

# Lowercase all text in the "text" column
df["Review_Title"] = df["Review_Title"].str.lower()
df["Review"] = df["Review"].str.lower()
df["Seat Type"] = df["Seat Type"].str.lower()
df["Route"] = df["Route"].str.lower()
df["Airline Name"] = df["Airline Name"].str.lower()
df["Type Of Traveller"] = df["Type Of Traveller"].str.lower()

"""TOKENIZATION:

Tokenization is a fundamental step in natural language processing (NLP) that involves breaking down text into smaller units, typically words or subwords.
1.  word_tokenize() is a function from the NLTK (Natural Language Toolkit) library that tokenizes text into individual words or tokens.
2.   By using apply(), the tokenization function is applied element-wise to each text entry in the specified columns, resulting in a list of tokens for each entry.

"""

# Download for tokenization, stemming & lemmatization
nltk.download('punkt')
nltk.download('wordnet')

# Tokenize two specific columns
df["Review_Title"] = df["Review_Title"].apply(word_tokenize)
df["Review"] = df["Review"].apply(word_tokenize)

"""REMOVAL OF NUMERIC NUMBERS:

Removing numeric characters is a common preprocessing step in NLP to eliminate numerical noise from textual data.
1.   Function Definition: remove_numeric_chars() is a Python function that takes a string text as input.
2.   List Comprehension: Within the function, a list comprehension is used to iterate over each character in the input text. For each character, it checks whether it is a digit using char.isdigit().
3.   Character Removal: If the character is not a digit, it is included in the resulting list. Otherwise, it is skipped.
4. Joining Characters: Finally, ''.join() is used to concatenate the characters in the resulting list back into a single string, effectively removing all numeric characters.


"""

# Define a function to remove numeric characters
def remove_numeric_chars(text):
  return ''.join([char for char in text if not char.isdigit()])

df["Review_Title"] = df["Review_Title"].apply(remove_numeric_chars)
df["Review"] = df["Review"].apply(remove_numeric_chars)

"""REMOVAL OF STOPWORDS:

Stopwords are common words in a language that often do not carry significant meaning and are typically removed during text preprocessing in NLP tasks.

1. Stopwords Loading: The code first loads a list of English stopwords using the stopwords.words('english') function from the NLTK library. This list contains common English stopwords such as "the", "is", "and", etc.
2. Splitting and Filtering: Within the lambda function, each text entry in the column is split into individual words using x.split(). Then, a list comprehension is used to iterate over each word and retain only those words that are not present in the stop_words list.
3. Joining Words: The remaining words are joined back into a single string using ' '.join()

"""

# Download the stopwords list
nltk.download('stopwords')

# Load the stopwords
stop_words = stopwords.words('english')

# Remove stop words
df["Review_Title"] = df["Review_Title"].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
df["Review"] = df["Review"].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

"""STEMMING & LEMMATIZATION:

Stemming and lemmatization are common text normalization techniques in natural language processing (NLP) that aim to reduce words to their base or root forms.

1. Word Tokenization: The text in each column is split into individual words using x.split().
2. Stemming Operation: For each word, stemming is applied using the stem() method of the stemming object (stemmer), which reduces the word to its base form.
3. Joining Words: The stemmed words are then joined back into a single string using ' '.join().
"""

# Initialize the stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Stem the words
df["Review_Title"] = df["Review_Title"].astype(str)
df["Review_Title"] = df["Review_Title"].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))
df["Review"] = df["Review"].astype(str)
df["Review"] = df["Review"].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))

# Lemmatize the words
df["Review_Title"] = df["Review_Title"].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))
df["Review"] = df["Review"].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))

# Display the first few rows of the DataFrame
df.head(20)