import requests
import os
token = os.getenv("GITHUB_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
print(TMDB_API_KEY is not None)

print(token is not None)

def search_movie(api_key: str, query: str) -> dict:
    url = f"https://api.themoviedb.org/3/search/movie"
    parameter = {"api_key": api_key, "query" : query}
    response = requests.get(url, params=parameter)

    if response.status_code ==200:
        data = response.json()

        results = data.get("results", [])


        if results:
            return results[0]

    return {}


def get_github_user(token: str, username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"} 
    response = requests.get(url, headers=headers)



    if response.status_code ==200:
        return response.json()

    return{}

def create_gist(token: str, description: str, filename: str, content: str) -> str:
    url = f"https://api.github.com/gists"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "description": description,
        "public": True,
        "files": {
            filename: {
                "content": content
            }
        }

    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return response.json().get("id", "")

    return ""

def delete_gist(token: str, gist_id: str) -> bool:
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.status_code == 204


def search_movie(api_key: str, query: str) -> dict:
    url = f"https://api.themoviedb.org/3/search/movie"
    parameter = {"api_key": api_key, "query" : query}
    response = requests.get(url, params=parameter)

    if response.status_code ==200:
        data = response.json()

        results = data.get("results", [])


        if results:
            return results[0]

    return {}


def get_github_user(token: str, username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"} 
    response = requests.get(url, headers=headers)



    if response.status_code ==200:
        return response.json()

    return{}

def create_gist(token: str, description: str, filename: str, content: str) -> str:
    url = f"https://api.github.com/gists"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "description": description,
        "public": True,
        "files": {
            filename: {
                "content": content
            }
        }

    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return response.json().get("id", "")

    return ""

def delete_gist(token: str, gist_id: str) -> bool:
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)

    return response.status_code == 204

result = search_movie(TMDB_API_KEY, "Batman")
print(result)

result = search_movie(TMDB_API_KEY, "Moana")
print(result)

