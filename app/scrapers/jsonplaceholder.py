import requests

def fetch_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    res = requests.get(url)
    return res.status_code, res.json()