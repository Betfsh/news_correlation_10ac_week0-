import pandas as pd
import yake
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

rating_data = pd.read_csv('"/home/b/Desktop/Tademy/Cohort_B/Week_0/Technical Content/archive/rating.csv')  

stopwords = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [token for token in tokens if token.lower() not in stopwords]
    
    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text


kw_extractor = yake.KeywordExtractor()
keywords = []

for article in rating_data['article']:
    preprocessed_text = preprocess_text(article)
    extracted_keywords = kw_extractor.extract_keywords(preprocessed_text)
    keywords.append([kw for kw, _ in extracted_keywords])
    
rating_data['keywords'] = keywords

