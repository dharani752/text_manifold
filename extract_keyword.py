import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import string
# Downloading required nltk data
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')


def ex_keywords(text):
    tokens = word_tokenize(text)
    
    # Removing stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # Lemmatizing the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Counting the frequency of each token
    token_counts = Counter(tokens)

    # punctuations 
    punctuations = '''!()-[]{};:'`’"“”\,<>./?@#$%^&*_~'''
    
    # Sorting the tokens by their frequency
    sorted_tokens = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)

    sorted_tokens1=[]
    for i in sorted_tokens:
        if i[0] not  in punctuations:
            sorted_tokens1.append(i)


    # Extracting the top 10 keywords
    top_keywords = [token[0] for token in sorted_tokens1[:10]]

    return top_keywords