import requests

def main(url):
    try:
        response = requests.get(url)
        return 1
    except requests.exceptions.ConnectionError:
        return 0

# print("HTTPS")
# print(main("https://www.google.com"))
# print(main('https://expired.badssl.com/'))
# print(main('https://self-signed.badssl.com/'))