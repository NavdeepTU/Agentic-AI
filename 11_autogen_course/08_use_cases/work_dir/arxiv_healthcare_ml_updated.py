# filename: arxiv_healthcare_ml_updated.py

import requests

# Define the search query
query = "machine learning in healthcare"

# Make the API request
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=5"
response = requests.get(url)

# Check if the response is valid
if response.status_code == 200 and response.text:
    try:
        data = response.json()
        papers = data['feed']['entry']

        # Extract and display relevant information
        for paper in papers:
            title = paper['title']
            authors = ", ".join(author['name'] for author in paper.get('author', []))
            abstract = paper.get('summary', 'No abstract available')
            link = paper['id']

            print(f"Title: {title}\nAuthors: {authors}\nAbstract: {abstract}\nLink: {link}\n")
    except Exception as e:
        print("An error occurred while processing the response:", e)
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)