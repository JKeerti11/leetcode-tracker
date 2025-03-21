import requests

def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Test the API with your username
username = "https://leetcode.com/u/keertij/"
data = fetch_leetcode_stats(username)
print(data)
