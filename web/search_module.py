import requests

def search(query):
    url = f"https://cse.google.com/cse.js?cx=6207aea4467e149de&q={query}"
    response = requests.get(url)
    data = response.json()

    search_results = []

    for item in data.get('items', []):
        result = {
            'name': item.get('title'),
            'website': item.get('link'),
            # Customize the fields below based on your search engine settings
            'contact_name': '',
            'contact_email': '',
            'contact_phone': ''
        }
        search_results.append(result)

    return search_results

