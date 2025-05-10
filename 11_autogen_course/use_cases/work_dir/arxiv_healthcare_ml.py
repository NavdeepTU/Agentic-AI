# filename: arxiv_healthcare_ml.py

import requests

# Define the search query
query = "machine learning in healthcare"

# Make the API request
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=5"
response = requests.get(url)

# Parse the JSON response
data = response.json()
papers = data['feed']['entry']

# Extract and display relevant information
for paper in papers:
    title = paper['title']
    authors = ", ".join(author['name'] for author in paper.get('author', []))
    abstract = paper.get('summary', 'No abstract available')
    link = paper['id']
    
    print(f"Title: {title}\nAuthors: {authors}\nAbstract: {abstract}\nLink: {link}\n")