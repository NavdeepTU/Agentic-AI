# filename: arxiv_healthcare_ml_encoded.py

import feedparser
import urllib.parse

# Define the search query
query = "machine learning in healthcare"

# Encode the query for the URL
encoded_query = urllib.parse.quote(query)

# Make the API request
url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&max_results=5"
response = feedparser.parse(url)

# Check if the response is valid
if response.entries:
    papers = response.entries

    # Extract and display relevant information
    for paper in papers:
        title = paper.title
        authors = ", ".join(author.name for author in paper.authors)
        abstract = paper.summary
        link = paper.link

        print(f"Title: {title}\nAuthors: {authors}\nAbstract: {abstract}\nLink: {link}\n")
else:
    print("No entries found for the query.")