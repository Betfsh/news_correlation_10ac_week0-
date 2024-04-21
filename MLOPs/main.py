from keyword_extractor import get_keyword_similarity

# File path to rating_data.csv
data_path = '/home/b/Desktop/Tademy/Cohort_B/Week_0/Technical Content/archive/rating.csv'

# Get similarity scores
similarities = get_keyword_similarity(data_path)

# Display similarity scores
for index, similarity in enumerate(similarities):
    print(f"Similarity score for article {index + 1}: {similarity}")