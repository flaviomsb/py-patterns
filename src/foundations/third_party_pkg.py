import requests


def ping_gh_api():
    response = requests.get("https://api.github.com")
    return response


print(ping_gh_api())
