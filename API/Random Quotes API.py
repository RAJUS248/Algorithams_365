import urllib.request, json

def get_quote():
    url = "https://zenquotes.io/api/random"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    q = data[0]['q']
    a = data[0]['a']
    print(f'\n "{q}"\n   — {a}')

if __name__ == "__main__":
    get_quote()
