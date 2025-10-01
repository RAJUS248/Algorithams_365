import urllib.request, json

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    if data['type'] == 'single':
        print(data['joke'])
    elif data['type'] == 'twopart':
        print(data['setup'])
        print(data['delivery'])

if __name__ == "__main__":
    get_joke()
