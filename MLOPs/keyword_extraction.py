import yake
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def preprocess_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stopwords_list = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stopwords_list]
    
    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

def extract_keywords(text):
    # Preprocess the text
    preprocessed_text = preprocess_text(text)
    
    # Initialize the YAKE keyword extractor
    kw_extractor = yake.KeywordExtractor()

    # Extract keywords from the preprocessed text
    extracted_keywords = kw_extractor.extract_keywords(preprocessed_text)
    
    # Keep only the keywords (ignore scores)
    keywords = [keyword for keyword, _ in extracted_keywords]
    
    return keywords

def calculate_similarity(keywords_headline, keywords_body):
    # Convert the keyword lists to sets
    set_headline = set(keywords_headline)
    set_body = set(keywords_body)
    
    # Calculate the Jaccard similarity between the sets
    similarity = len(set_headline.intersection(set_body)) / len(set_headline.union(set_body))
    
    return similarity

def get_keyword_similarity(data_path):
    # Read the CSV file into a DataFrame
    rating_data = pd.read_csv(data_path)
    
    similarities = []
    
    # Iterate over each row and calculate similarity
    for index, row in rating_data.iterrows():
        headline = row['headline']
        body = row['body']
        
        # Extract keywords from the headline and body
        keywords_headline = extract_keywords(headline)
        keywords_body = extract_keywords(body)
        
        # Calculate the similarity between the keyword sets
        similarity = calculate_similarity(keywords_headline, keywords_body)
        
        similarities.append(similarity)
    
    return similarities

    
   





