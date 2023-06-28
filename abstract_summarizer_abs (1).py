import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Define the input text to be summarized
#text = "India is known by many names. Some call it Bharat, while others call it Hindustan. India is the worlds seventh largest country and home to around 1.3 billion people, which stands as the second most populated country in the world. Once under the colonial rule of the British, India is now the worlds largest democracy"

def abstract_summarizer(raw_text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(raw_text)

    # Remove stop words and lemmatize the words in the sentences
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    cleaned_sentences = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]
        cleaned_sentences.append(' '.join(words))

    # Join the cleaned sentences back into a single string
    cleaned_text = ' '.join(cleaned_sentences)

    # Use a pre-trained NLP model to generate the summary
    from transformers import pipeline
    summarizer = pipeline('summarization')
    summary = summarizer(cleaned_text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']

    return summary

#print(abstract_summarizer(text))